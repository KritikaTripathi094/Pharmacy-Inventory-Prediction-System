import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv(r"C:\Users\L E N O V O\Desktop\pharmacy_sales_daily.csv")

# Converting the date column into the real date as py sees current date as String
df["datum"] = pd.to_datetime(df["datum"])

# Checking the data type of date we changed
print(df.info())

print(df.tail())

