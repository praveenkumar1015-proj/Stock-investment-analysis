import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# 1. Load the dataset from the path
# ================================
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\nifty500_clean.csv")

# ================================
# 2. Data Cleaning
# ================================
def clean_data(df):
    df.fillna(0, inplace=True)
    print("Missing values handled")
    return df


# ================================
# 3. Top Growth Stocks
# ================================
def get_top_growth(df):
    top_growth = df.sort_values(
        by="365 Day Percentage Change",
        ascending=False
    ).head(10)

    print("\n Top 10 Growth Stocks:")
    print(top_growth[["Company Name", "365 Day Percentage Change"]])

    return top_growth

# ================================
# 4. Top Investment Stocks
# ================================
def get_top_investment(df):
    top_investment = df.sort_values(
        by="Investment_Score",
        ascending=False
    ).head(10)

    print("\n Top Investment Stocks:")
    print(top_investment[["Company Name", "Investment_Score"]])

    return top_investment

# ================================
# 5. Industry Analysis
# ================================
def industry_analysis(df):
    industry_growth = df.groupby("Industry")[
        "365 Day Percentage Change"
    ].mean().sort_values(ascending=False)

    print("\n Top Performing Industries:")
    print(industry_growth.head(10))

    return industry_growth

# ================================
# 6. Visualization
# ================================
def plot_industry_growth(industry_growth):
    industry_growth.head(10).plot(kind='bar')
    plt.title("Top Performing Industries")
    plt.xlabel("Industry")
    plt.ylabel("Average Growth")
    plt.savefig(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\industry_growth.png")
    plt.close()


def plot_risk_vs_growth(df):
    plt.scatter(df["Risk %"], df["365 Day Percentage Change"])
    plt.title("Risk vs Growth")
    plt.xlabel("Risk %")
    plt.ylabel("Growth %")
    plt.savefig(r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\risk_vs_growth.png")
    plt.close()

# ================================
# 7. Save Data
# ================================
def save_data(df):
    df.to_csv("stocks_processed.csv", index=False)
    print("Processed data saved")


# ================================
# 8. Main Function
# ================================
def main():
    file_path = r"C:\Users\HP\OneDrive\Documents\Project for Investment Analysis\nifty500_clean.csv"

    df = pd.read_csv(file_path)
    df = clean_data(df)

    get_top_growth(df)
    get_top_investment(df)

    industry_growth = industry_analysis(df)

    plot_industry_growth(industry_growth)
    plot_risk_vs_growth(df)

    save_data(df)


# ================================
# Run Program
# ================================
if __name__ == "__main__":
    main()