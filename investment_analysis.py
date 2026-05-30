import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the path
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\nifty500_clean.csv")

# Step 2: Show first rows
print("Dataset Preview:")
print(df.head())

# Step 3: Check data info
print("\nDataset Info:")
print(df.info())

# Step 4: Handle missing values
df.fillna(0, inplace=True)

# Step 5: Top 10 Growth Stocks
top_growth = df.sort_values(by="365 Day Percentage Change", ascending=False).head(10)

print("\nTop 10 Growth Stocks:")
print(top_growth[["Company Name", "365 Day Percentage Change"]])

# Step 6: Top Investment Stocks
top_investment = df.sort_values(by="Investment_Score", ascending=False).head(10)

print("\nTop Investment Stocks:")
print(top_investment[["Company Name", "Investment_Score"]])

# Step 7: Industry Analysis
industry_growth = df.groupby("Industry")["365 Day Percentage Change"].mean().sort_values(ascending=False)

print("\nTop Performing Industries:")
print(industry_growth.head(10))

# Step 8: Plot Industry Growth
industry_growth.head(10).plot(kind="bar")
plt.title("Top Performing Industries")
plt.xlabel("Industry")
plt.ylabel("Average Growth")
plt.savefig(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\industry_growth.png")
plt.close()

# Step 9: Risk vs Growth Plot
plt.scatter(df["Risk %"], df["365 Day Percentage Change"])
plt.title("Risk vs Growth")
plt.xlabel("Risk %")
plt.ylabel("Growth %")
plt.savefig(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\risk_vs_growth.png")
plt.close()

# Step 10: Save processed dataset
df.to_csv("stocks_processed.csv", index=False)

print("\nProcessed dataset saved successfully!")