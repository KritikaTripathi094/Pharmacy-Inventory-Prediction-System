import os
import pandas as pd

# =====================================================
# STEP 04: CREATE TARGET VARIABLES USING QUARTILES
# =====================================================

# 1. Load cleaned dataset
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_cleaned.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Could not find {input_path}")

df = pd.read_csv(input_path)

# 2. List of medicine categories
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

print("========================================================")
print("CREATING INDIVIDUAL MEDICINE DEMAND CLASSES")
print("USING Q1, Q2 (MEDIAN), AND Q3")
print("========================================================")

# 3. Create demand class for each medicine
for drug in drug_cols:

    # Calculate quartiles
    q1 = df[drug].quantile(0.25)
    q2 = df[drug].median()
    q3 = df[drug].quantile(0.75)

    demand_col = drug + "_Demand"

    # Classify demand
    def classify(value):
        if value <= q1:
            return 0      # Low Demand
        elif value <= q3:
            return 1      # Normal Demand
        else:
            return 2      # High Demand

    df[demand_col] = df[drug].apply(classify)

    # Display results
    print(f"\nMedicine : {drug}")
    print(f"Q1 (25%)      : {q1:.2f}")
    print(f"Q2 (Median)   : {q2:.2f}")
    print(f"Q3 (75%)      : {q3:.2f}")

    print("\nDemand Class Distribution")
    print("0 = Low Demand")
    print("1 = Normal Demand")
    print("2 = High Demand")
    print(df[demand_col].value_counts().sort_index())

    print("-" * 50)

# 4. Save updated dataset
output_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_with_target.csv"

df.to_csv(output_path, index=False)

print("\n========================================================")
print("STEP 04 COMPLETED SUCCESSFULLY")
print("Individual demand classes created for all medicines.")
print(f"Updated dataset saved to:\n{output_path}")
print("========================================================")