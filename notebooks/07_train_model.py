import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =====================================================
# STEP 07: TRAINING THE RANDOM FOREST MODEL
# =====================================================

# 1. Loading the dataset from Step 06
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\pharmacy_training_dataset.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Could not find {input_path}!")

df = pd.read_csv(input_path)

# 2. Selecting the features and target variable
features = [
    "Medicine_Encoded",
    "Year",
    "Month",
    "Weekday_Encoded"
]

X = df[features]
y = df["Demand"]

# 3. Splitting the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# stratify=y keeps the same proportion of Low,
# Normal and High demand records in both datasets.

print("==============================================")
print("TRAINING THE RANDOM FOREST MODEL")
print("==============================================")
print(f"Training set size : {X_train.shape[0]} records")
print(f"Testing set size  : {X_test.shape[0]} records\n")

# 4. Initializing and training the Random Forest model
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(X_train, y_train)

# 5. Saving the trained model
model_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\models\pharmacy_rf_model.pkl"

joblib.dump(model, model_path)

print("Model saved successfully!")
print(f"Saved to: {model_path}\n")

# 6. Evaluating the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("==============================================")
print("MODEL PERFORMANCE RESULTS")
print("==============================================")
print(f"Overall Model Accuracy : {accuracy:.2%}\n")

print("Detailed Classification Report")
print(classification_report(y_test, y_pred))

print("==============================================")
print("STEP 07 COMPLETED SUCCESSFULLY")
print("==============================================")