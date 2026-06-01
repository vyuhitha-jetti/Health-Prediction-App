def predict_health(glucose, haemoglobin, cholesterol):

    result = []


    if glucose > 140:
        result.append(
            "High Diabetes Risk"
        )


    if cholesterol > 240:
        result.append(
            "High Cholesterol Risk"
        )


    if haemoglobin < 12:
        result.append(
            "Anaemia Risk"
        )


    if len(result)==0:

        return "Patient health condition looks normal"


    return ", ".join(result)