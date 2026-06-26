import pandas as pd

# Loading original dataset
df = pd.read_csv(r"C:\Users\L E N O V O\Desktop\pharmacy_sales_daily.csv")

# Converting date column as for now it takes this as string
df["datum"] = pd.to_datetime(df["datum"])

# Removing Hour column because not needed
df.drop(columns=["Hour"], inplace=True)

# Saving cleaned dataset so I dont have to repeat in every step
df.to_csv(r"C:\Users\L E N O V O\Desktop\pharmacy_sales_daily_cleaned.csv", index=False)

print("✅ Data preprocessing completed successfully!")
print("Cleaned dataset saved as: data/sales_daily_cleaned.csv")
print(df.head())