import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =====================================================
# STEP 08: HYPERPARAMETER TUNING
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

print("=======================================================")
print("RANDOM FOREST HYPERPARAMETER TUNING")
print("=======================================================")

# 4. Trying different numbers of trees
tree_values = [10, 50, 100, 200]

best_accuracy = 0
best_tree = 0

for trees in tree_values:

    model = RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print(f"Trees: {trees:<3}  Accuracy: {accuracy:.2%}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_tree = trees

print("\n=======================================================")
print("BEST HYPERPARAMETER")
print("=======================================================")
print(f"Best Number of Trees : {best_tree}")
print(f"Best Accuracy        : {best_accuracy:.2%}")
print("=======================================================")