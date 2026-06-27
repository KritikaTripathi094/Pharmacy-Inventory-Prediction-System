import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Loading the dataset from step 5
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_encoded.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Could not find {input_path}!")

df = pd.read_csv(input_path)

# 2. Selecting Features (X) and Target (y)
# We use Year, Month, and our brand new Weekday_Encoded to predict High_Demand
features = ["Year", "Month", "Weekday_Encoded"]
X = df[features]
y = df["High_Demand"]

# 3. Splitting the data into 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#stratify=y tells Python to keep the same proportion of High Demand and Low Demand records in both the training and testing sets

print("==============================================")
print("🤖 TRAINING THE RANDOM FOREST MODEL")
print("==============================================")
print(f"Training set size: {X_train.shape[0]} days")
print(f"Testing set size: {X_test.shape[0]} days\n")

# 4. Initializing and Training the Random Forest
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Saing the trained model
joblib.dump(model, r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\models\pharmacy_rf_model.pkl")

print("✅ Model saved successfully!")

# 5. Evaluating how well the model learns
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("==============================================")
print("📊 MODEL PERFORMANCE RESULTS")
print("==============================================")
print(f"Overall Model Accuracy: {accuracy:.2%}\n")
print("Detailed Classification Report:")
print(classification_report(y_test, y_pred))
print("==============================================")