import os
import pandas as pd

# =====================================================
# STEP 06: PREPARING TRAINING DATASET
# =====================================================

# 1. Loading the dataset from Step 05
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_encoded.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Could not find {input_path}")

df = pd.read_csv(input_path)

print("==============================================")
print("STEP 06 : PREPARING TRAINING DATASET")
print("==============================================")

# List of all medicine categories
drug_cols = [
    "M01AB",
    "M01AE",
    "N02BA",
    "N02BE",
    "N05B",
    "N05C",
    "R03",
    "R06"
]

# Creating a number for each medicine
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

# Creating an empty list to store the new training dataset
training_rows = []

# Going through every row of the dataset
for _, row in df.iterrows():

    # Going through each medicine one by one
    for medicine in drug_cols:

        # Adding one new row for each medicine
        training_rows.append({

            "Medicine": medicine,

            "Medicine_Encoded": medicine_map[medicine],

            "Year": row["Year"],

            "Month": row["Month"],

            "Weekday_Encoded": row["Weekday_Encoded"],

            "Demand": row[f"{medicine}_Demand"]

        })

# Creating the final training dataset
training_df = pd.DataFrame(training_rows)

# Displaying the first 10 records
print("\nFirst 10 Records")
print("----------------------------------------------")
print(training_df.head(10))

# Displaying dataset information
print("\nDataset Information")
print("----------------------------------------------")
print(f"Total Records : {len(training_df)}")
print(f"Total Features: {len(training_df.columns)}")

# Displaying medicine encoding
print("\nMedicine Encoding")
print("----------------------------------------------")
for medicine, code in medicine_map.items():
    print(f"{medicine} --> {code}")

# Saving the final training dataset
output_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\pharmacy_training_dataset.csv"

training_df.to_csv(output_path, index=False)

print("\n==============================================")
print("STEP 06 COMPLETED SUCCESSFULLY")
print("==============================================")
print(f"Training dataset saved to:\n{output_path}")