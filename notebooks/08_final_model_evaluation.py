import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ---------------------------------------
# Load Dataset
# ---------------------------------------

input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_encoded.csv"

df = pd.read_csv(input_path)

# ---------------------------------------
# Features and Target
# ---------------------------------------

features = ["Year", "Month", "Weekday_Encoded"]

X = df[features]
y = df["High_Demand"]

# ---------------------------------------
# Train-Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ---------------------------------------
# Final Model
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------------------
# Predictions
# ---------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------
# Accuracy
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("="*60)
print("FINAL MODEL EVALUATION")
print("="*60)

print(f"\nAccuracy : {accuracy:.2%}\n")

print("Classification Report")
print(classification_report(y_test, y_pred))

# ---------------------------------------
# Confusion Matrix
# ---------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Low Demand","High Demand"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")

os.makedirs("report/figures", exist_ok=True)

plt.savefig("report/figures/confusion_matrix.png", dpi=300)

plt.show()

# ---------------------------------------
# Feature Importance
# ---------------------------------------

importance = pd.DataFrame({

    "Feature":features,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")

print(importance)

plt.figure(figsize=(6,4))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance Score")

plt.savefig("report/figures/feature_importance.png", dpi=300)

plt.show()