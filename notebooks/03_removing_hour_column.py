import pandas as pd

df = pd.read_csv(r"C:\Users\L E N O V O\Desktop\pharmacy_sales_daily.csv")

df.drop(columns=["Hour"], inplace=True)

# Check dataset
print(df.info())
print(df.head())