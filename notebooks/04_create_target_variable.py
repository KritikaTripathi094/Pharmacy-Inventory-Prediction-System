import os
import pandas as pd


input_path = (
    r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_cleaned.csv"
   
)

if not os.path.exists(input_path):
    raise FileNotFoundError(
        f"Could not find {input_path}. Please check your folders!"
    )

df = pd.read_csv(input_path)

# List of the 8 core medicine categories
drug_cols = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]

# 2. Calculating Total Daily Sales volume of 8 med
df["Total_Sales"] = df[drug_cols].sum(axis=1)

# 3. Determining the baseline benchmark by calculating median
sales_threshold = df["Total_Sales"].median()

# Creating binary target variable
df["High_Demand"] = (df["Total_Sales"] > sales_threshold).astype(int)

#"The target variable assignment follows standard machine learning binary mapping, 
# where 0 acts as the negative class (Normal Demand, indicating sales equal to or below the baseline median) and 
# 1 acts as the positive class (High Demand, indicating sales exceeding the baseline median)."


# 4. Displaying the results
print("==============================================")
print("🎯 TARGET VARIABLE CREATION COMPLETED")
print("==============================================")
print(f"Calculated Median Daily Sales Threshold: {sales_threshold:.2f} units\n")
print("Target Variable Class Distribution:")
print(df["High_Demand"].value_counts())
print("==============================================")

# 5. Using the full absolute path for your output file
output_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_with_target.csv"
df.to_csv(output_path, index=False)

print(f"💾 Updated dataset saved cleanly to: {output_path}\n")