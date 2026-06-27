import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\L E N O V O\Desktop\Pharmacy_Inventory_AI\data\raw\pharmacy_sales_daily.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.isnull().sum())

print(df.describe())