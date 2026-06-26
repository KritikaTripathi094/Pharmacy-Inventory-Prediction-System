import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv(r"C:\Users\L E N O V O\Desktop\pharmacy_sales_daily.csv")
df["datum"] = pd.to_datetime(df["datum"])

# Defining the drug columns
drug_cols = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]

# Creating an output directory for the report visualisations
os.makedirs("eda_plots", exist_ok=True)

# 2. Calculating and displaying average sales
average_sales = df[drug_cols].mean()
print("--- Average Daily Sales of Medicines ---")
print(average_sales)

# 3. Ploting and saving the Bar Chart
plt.figure(figsize=(10, 5))
sns.barplot(x=average_sales.index, y=average_sales.values, palette="viridis")

plt.title("Average Daily Sales of Medicines")
plt.xlabel("Medicine Category")
plt.ylabel("Average Sales (Units)")
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("eda_plots/01_average_sales.png")
plt.close()
print("\n✅ Saved: eda_plots/01_average_sales.png")

# 4. Correlation Heatmap (Crucial to see which drugs sell together before feature selection)
plt.figure(figsize=(8, 6))
sns.heatmap(df[drug_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Medicine Sales Correlation")
plt.tight_layout()
plt.savefig("eda_plots/02_correlation_matrix.png")
plt.close()
print("✅ Saved: eda_plots/02_correlation_matrix.png")

print("\n🚀 EDA step completed successfully!")