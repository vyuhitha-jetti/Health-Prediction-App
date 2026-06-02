from flask import Flask,render_template,request,redirect

from models import db,Patient

from health_predictor import predict_health

from datetime import datetime

import re


app = Flask(__name__)
app.secret_key = "health_prediction_secret"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///health.db'
db.init_app(app)


with app.app_context():

    db.create_all()


def valid_email(email):

    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern,email)


@app.route("/")

def index():

    patients=Patient.query.all()

    return render_template(
        "index.html",
        patients=patients
    )


@app.route("/add",methods=['GET','POST'])

def add_patient():


    if request.method=="POST":


        name=request.form['name']

        dob=request.form['dob']

        email=request.form['email']

        if name.strip()=="":
            return "Name cannot be empty"
        
        if not name.replace(" ","").isalpha():
            return "Name must be alphabetic"
        
        if datetime.strptime(
            dob,"%Y-%m-%d"
        ).date()> datetime.today().date():
            return "Date of Birth cannot be in the future"
        
        if not valid_email(email):
            return"Please enter a valid Email Address"
        
        if(
            request.form['glucose'].strip()=="" or
            request.form['haemoglobin'].strip()=="" or
            request.form['cholesterol'].strip()==""
        ):
            return "Please fill all blood test details"
        

        try:

            glucose=float(request.form['glucose'])
        except ValueError:
            return "glucose value must be a number"
        
        try:

            haemoglobin=float(request.form['haemoglobin'])
        except ValueError:
            return "haemoglobin value must be a number" 

        try:   

            cholesterol=float(request.form['cholesterol'])
        except ValueError:
            return "cholesterol value must be a number"



        remarks=predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        patient=Patient(

            full_name=name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=remarks
        )


        db.session.add(patient)
        db.session.commit()

        return redirect("/")


    return render_template(
        "add_patient.html"
    )


@app.route("/delete/<int:id>")

def delete(id):

    patient=Patient.query.get(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect("/")


@app.route("/update/<int:id>",
methods=['GET','POST'])

def update(id):

    patient=Patient.query.get(id)

    if request.method=="POST":

        patient.full_name=request.form['name']

        patient.email=request.form['email']

        patient.glucose=float(
            request.form['glucose']
        )

        patient.haemoglobin=float(
            request.form['haemoglobin']
        )

        patient.cholesterol=float(
            request.form['cholesterol']
        )

        patient.remarks=predict_health(

            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        db.session.commit()

        return redirect("/")

    return render_template(
        "update_patient.html",
        patient=patient
    )


if __name__=="__main__":

    app.run(debug=True)