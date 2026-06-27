import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -------------------------------
# 1. Loading the dataset
# -------------------------------
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_encoded.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Dataset not found: {input_path}")

df = pd.read_csv(input_path)

# -------------------------------
# 2. Selecting  Features and Target
# -------------------------------
features = ["Year", "Month", "Weekday_Encoded"]

X = df[features]
y = df["High_Demand"]

# -------------------------------
# 3. Spliting Dataset
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("="*55)
print(" RANDOM FOREST HYPERPARAMETER TUNING ")
print("="*55)

results = []

# -------------------------------
# 4. Trying Different Numbers of Trees
# -------------------------------
tree_values = [10, 50, 100, 200]

for trees in tree_values:

    model = RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append([trees, accuracy])

    print(f"Trees: {trees:<3}  Accuracy: {accuracy:.2%}")

# -------------------------------
# 5. Finding Best Model
# -------------------------------
best_model = max(results, key=lambda x: x[1])

print("\n" + "="*55)
print(" BEST HYPERPARAMETER ")
print("="*55)

print(f"Best Number of Trees : {best_model[0]}")
print(f"Best Accuracy        : {best_model[1]:.2%}")