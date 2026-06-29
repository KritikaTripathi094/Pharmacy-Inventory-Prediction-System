import joblib
import os

# =====================================================
# Loading the trained Random Forest model
# =====================================================

model_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\models\pharmacy_rf_model.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Could not find {model_path}")

model = joblib.load(model_path)

# =====================================================
# Encoding dictionaries
# =====================================================

medicine_map = {
    "M01AB": 0,
    "M01AE": 1,
    "N02BA": 2,
    "N02BE": 3,
    "N05B": 4,
    "N05C": 5,
    "R03": 6,
    "R06": 7
}

weekday_map = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}

# =====================================================
# Predicting the demand
# =====================================================

def predict_demand(medicine, year, month, weekday):

    medicine_encoded = medicine_map[medicine]
    weekday_encoded = weekday_map[weekday]

    prediction = model.predict([[
        medicine_encoded,
        year,
        month,
        weekday_encoded
    ]])[0]

    if prediction == 0:
        return "Low Demand"

    elif prediction == 1:
        return "Normal Demand"

    else:
        return "High Demand"