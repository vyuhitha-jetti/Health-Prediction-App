# Health Prediction Application


## Project Description

The Health Prediction Application is a Python Flask based application designed to manage patient blood test records and predict possible health risks.

The application collects patient details such as full name, date of birth, email address, glucose level, haemoglobin level, and cholesterol level.

After entering valid patient information, the system analyzes the blood test values and generates health remarks indicating possible health conditions or disease risks.

The application provides CRUD operations where users can create, view, update, and delete patient records.


## Features

- Add new patient details
- View patient records
- Update existing records
- Delete patient records
- Email validation
- Date of birth validation
- Blood test value validation
- Generate health prediction remarks


## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Bootstrap


## Modules

### Backend
Flask handles application routes, validation, database operations, and prediction logic.

### Database
SQLite stores patient information and generated health remarks.

### Prediction
The health prediction module analyzes glucose, haemoglobin, and cholesterol values to generate possible risk remarks.


## How to Run the Project

1. Install dependencies

pip install -r requirements.txt


2. Run application

python app.py


3. Open browser

http://127.0.0.1:5000