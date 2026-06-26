import os
import pandas as pd

# 1. Loading the dataset from our previous step (step 4)
input_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_with_target.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Could not find {input_path}!")

df = pd.read_csv(input_path)

print("==============================================")
print("📊 BEFORE ENCODING: Text Days")
print("==============================================")
print(df[["Weekday Name"]].head(7))

# 2. Creating our day-to-number cheat sheet mapping
weekday_map = {
   "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}

# 3. Adding the brand-new numeric column using the mapping list
df["Weekday_Encoded"] = df["Weekday Name"].map(weekday_map)

print("\n==============================================")
print("🔢 AFTER ENCODING: Brand New Numeric Column Added")
print("==============================================")
print(df[["Weekday Name", "Weekday_Encoded"]].head(7))

# 4. Checking to make sure no days were missed or skipped
missing_counts = df["Weekday_Encoded"].isnull().sum()
print("----------------------------------------------")
print(f"Missing values in new column: {missing_counts}")
print("==============================================")

# 5. Saving this updated dataset down into a new file name
output_path = r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\processed\sales_daily_encoded.csv"
df.to_csv(output_path, index=False)

print(f"💾 Step 5 Complete! File saved cleanly to:\n{output_path}\n")