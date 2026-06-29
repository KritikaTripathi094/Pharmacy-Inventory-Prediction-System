import os
import joblib
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

# =====================================================
# STEP 09 : FINAL MODEL EVALUATION
# =====================================================

# 1. Loading the dataset
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

# 3. Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("============================================================")
print("FINAL MODEL EVALUATION")
print("============================================================")

# 4. Training the final model
model = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)

model.fit(X_train, y_train)

# 5. Saving the trained model
model_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\models\pharmacy_rf_model.pkl"
joblib.dump(model, model_path)

# 6. Predicting the testing data
y_pred = model.predict(X_test)

# 7. Calculating model accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy : {accuracy:.2%}\n")

# 8. Displaying classification report
print("Classification Report")
print(classification_report(y_test, y_pred))

# 9. Creating confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix")
print(cm)

# 10. Plotting confusion matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Low", "Normal", "High"]
)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix")

# Saving confusion matrix
confusion_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\report\figures\confusion_matrix.png"

plt.savefig(
    confusion_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"\nConfusion Matrix saved to:\n{confusion_path}")

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n============================================================")
print("FEATURE IMPORTANCE")
print("============================================================")
print(importance_df)

# Creating feature importance graph
plt.figure(figsize=(8,5))

bars = plt.barh(
    importance_df["Feature"],
    importance_df["Importance"],
    edgecolor="black"
)

plt.gca().invert_yaxis()

# Display percentages
for bar in bars:

    width = bar.get_width()

    plt.text(
        width + 0.003,
        bar.get_y() + bar.get_height()/2,
        f"{width*100:.2f}%",
        va="center"
    )

plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Features")

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save feature importance
feature_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\report\figures\feature_importance.png"

plt.savefig(
    feature_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"\nFeature Importance saved to:\n{feature_path}")

print("\n============================================================")
print("STEP 09 COMPLETED SUCCESSFULLY")
print("============================================================")