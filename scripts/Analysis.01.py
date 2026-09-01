import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option("display.max_columns", None)

print("Libraries imported successfully!")

# =========================================================
# 1. LOAD DATASET
# =========================================================
df=pd.read_csv("../data/Ecommerce_Sales.csv")
print("Dataset loaded successfully!")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Shape of the dataset
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Data types
print("\nData Types:")
print(df.dtypes)

# =========================================================
# 2. DATA CLEANING
# =========================================================

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Records
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("Duplicate rows removed Successfully!")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# =========================================================
# 3. SUMMARY STATISTICS
# =========================================================

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nNumber of Unique Values:")
print(df.nunique())

# =========================================================
# 4. CONVERT DATE COLUMN
# =========================================================

df["order_date"] = pd.to_datetime(df["order_date"])    

print("\nOrder date converted successfully!")
print(df["order_date"].dtype)

# =========================================================
# 5. CATEGORY-WISE SALES
# =========================================================

category_sales = (
    df.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    )

print("\nCategory-wise Total Sales:")
print(category_sales)

# Category Sales Chart

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/category_sales.png")
plt.show()


# =========================================================
# 6. ORDERS BY REGION
# =========================================================

region_orders = df["region"].value_counts()
print("\nOrders by Region:")
print(region_orders)


plt.figure(figsize=(8, 5))

region_orders.plot(kind="bar")

plt.title("Number of Orders by Region")
plt.xlabel("Region")
plt.ylabel("Number of Orders")

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../charts/region_orders.png")
plt.show()

# =========================================================
# 7. PAYMENT METHOD ANALYSIS
# =========================================================

payment_counts = df["payment_method"].value_counts()

print("\nPayment Method Distribution:")
print(payment_counts)


plt.figure(figsize=(7, 7))

payment_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
    )

plt.ylabel("")
plt.title("Payment Method Distribution")

plt.tight_layout()
plt.show()

# =========================================================
# 8. MONTHLY SALES TREND
# =========================================================

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .sum()
    )

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(12, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/monthly_sales.png")
plt.show()

# ==========================================
# 9. Top 10 Products by Sales 
# ==========================================

product_sales = (
    df.groupby("product_id")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

top_10_products = product_sales.head(10)
print(top_10_products)

plt.figure(figsize=(10, 6))

top_10_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product ID")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/top_10_products.png")
plt.show()

# =========================================================
# 10. REGION-WISE SALES
# =========================================================

region_sales = (
    df.groupby("region")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRegion-wise Total Sales:")
print(region_sales)


plt.figure(figsize=(8, 5))

ax = region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)

# Add values on bars
for i, value in enumerate(region_sales):
    ax.text(
        i,
        value,
        f"{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

# =========================================================
# 11. RETURN ANALYSIS
# =========================================================

return_counts = df["returned"].value_counts()
print("\nReturn Status:")
print(return_counts)

return_percentage =(
    df["returned"]
    .value_counts(normalize=True)*100
)

print("\nReturn Percentage:")
print(return_percentage)


plt.figure(figsize=(7, 5))
return_counts.plot(kind="bar")

plt.title("Order Return Status")
plt.xlabel("Returned")
plt.ylabel("Number of Orders")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =========================================================
# 12. RETURN RATE BY CATEGORY
# =========================================================

category_orders = df.groupby("category").size()

category_returns =(
    df[df["returned"] == "Yes"]
    .groupby("category")
    .size()
)

category_return_rate = (
    category_returns
    .div(category_orders)
    .mul(100)
    .sort_values(ascending=False)
)

print("\nReturn Rate by Category:")
print(category_return_rate)


plt.figure(figsize=(9, 5))

category_returns.plot(kind="bar")

plt.title("Returned Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Returned Orders")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/category_return_rate.png")
plt.show()

# =========================================================
# 13. PROFIT ANALYSIS
# =========================================================
# Average profit_margin value by category

category_profit = (
    df.groupby("category")["profit_margin"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Profit Margin Value by Category:")
print(category_profit)


plt.figure(figsize=(9, 5))

category_profit.plot(kind="bar")

plt.title("Average Profit Margin Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Profit Margin Value")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/category_profit.png")
plt.show()


# Total profit_margin value by category

category_profit_total = (
    df.groupby("category")["profit_margin"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Profit Margin Value by Category:")
print(category_profit_total)


plt.figure(figsize=(9, 5))

category_profit_total.plot(kind="bar")

plt.title("Total Profit Margin Value by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit Margin Value")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================================================
# 14. AGE GROUP ANALYSIS
# =========================================================

age_bins = [17, 25, 35, 45, 55, 65, 69]

age_labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66-69"
]

df["Age_Group"] = pd.cut(
    df["customer_age"],
    bins=age_bins,
    labels=age_labels
)

# Orders by age group

age_group_orders = (
    df["Age_Group"]
    .value_counts()
    .sort_index()
)

print("\nOrders by Age Group:")
print(age_group_orders)


plt.figure(figsize=(9, 5))

age_group_orders.plot(kind="bar")

plt.title("Number of Orders by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by age group

age_group_sales = (
    df.groupby("Age_Group", observed=True)["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Age Group:")
print(age_group_sales)


plt.figure(figsize=(9, 5))

age_group_sales.plot(kind="bar")

plt.title("Total Sales by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../charts/age_group_sales.png")
plt.show()

# =========================================================
# 15. CUSTOMER GENDER ANALYSIS
# =========================================================

gender_orders = df["customer_gender"].value_counts()

print("\nOrders by Customer Gender:")
print(gender_orders)


plt.figure(figsize=(8, 5))

gender_orders.plot(kind="bar")

plt.title("Number of Orders by Customer Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Number of Orders")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Gender-wise sales

gender_sales = (
    df.groupby("customer_gender")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Customer Gender:")
print(gender_sales)


plt.figure(figsize=(8, 5))

gender_sales.plot(kind="bar")

plt.title("Total Sales by Customer Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Total Sales")

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../charts/gender_sales.png")
plt.show()

# =========================================================
# 16. AVERAGE ORDER VALUE
# =========================================================

gender_aov = (
    df.groupby("customer_gender")["total_amount"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Order Value by Gender:")
print(gender_aov)


plt.figure(figsize=(8, 5))

gender_aov.plot(kind="bar")

plt.title("Average Order Value by Customer Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Average Order Value")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# =========================================================
# 17. SALES AND PROFIT COMPARISON
# =========================================================

category_performance = (
    df.groupby("category")
    .agg(
        Total_Sales=("total_amount", "sum"),
        Average_Profit_Margin=("profit_margin", "mean"),
        Total_Profit_Margin=("profit_margin", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nCategory Performance:")
print(category_performance)

# =========================================================
# 18. CORRELATION ANALYSIS
# =========================================================

numeric_columns = [
    "price",
    "discount",
    "quantity",
    "delivery_time_days",
    "total_amount",
    "shipping_cost",
    "profit_margin",
    "customer_age"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Correlation Heatmap

plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("../charts/correlation_heatmap.png")
plt.show()

# =========================================================
# 19. TOTAL AMOUNT VS PROFIT MARGIN
# =========================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="total_amount",
    y="profit_margin"
)

plt.title("Total Amount vs Profit Margin")
plt.xlabel("Total Amount")
plt.ylabel("Profit Margin")

plt.tight_layout()
plt.savefig("../charts/sales_vs_profit.png")
plt.show()

# =========================================================
# 20. MONTHLY ORDER TREND
# =========================================================

monthly_orders = (
    df.groupby(df["order_date"].dt.to_period("M"))
    .size()
)

print("\nMonthly Orders:")
print(monthly_orders)


plt.figure(figsize=(12, 5))

monthly_orders.plot(kind="line", marker="o")

plt.title("Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================================================
# 21. MONTHLY AVERAGE ORDER VALUE
# =========================================================

monthly_aov = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .mean()
)

print("\nMonthly Average Order Value:")
print(monthly_aov)


highest_month = monthly_aov.idxmax()
highest_aov = monthly_aov.max()

lowest_month = monthly_aov.idxmin()
lowest_aov = monthly_aov.min()

print("\nHighest Monthly AOV:")
print(highest_month, round(highest_aov, 2))
print("\nLowest Monthly AOV:")
print(lowest_month, round(lowest_aov, 2))

# =========================================================
# 22. FINAL SUMMARY
# =========================================================

print("\n========================================")
print("FINAL BUSINESS SUMMARY")
print("========================================")

print(
    "\nHighest Sales Category:",
    category_sales.idxmax(),
    round(category_sales.max(), 2)
)

print(
    "Lowest Sales Category:",
    category_sales.idxmin(),
    round(category_sales.min(), 2)
)

print(
    "Highest Order Region:",
    region_orders.idxmax(),
    region_orders.max()
)

print(
    "Lowest Order Region:",
    region_orders.idxmin(),
    region_orders.min()
)

print(
    "Highest Return Rate Category:",
    category_return_rate.idxmax(),
    round(category_return_rate.max(), 2)
)

print(
    "Lowest Return Rate Category:",
    category_return_rate.idxmin(),
    round(category_return_rate.min(), 2)
)

print(
    "Highest AOV Gender:",
    gender_aov.idxmax(),
    round(gender_aov.max(), 2)
)

print(
    "Highest Sales Age Group:",
    age_group_sales.idxmax(),
    round(age_group_sales.max(), 2)
)

print(
    "Highest Monthly AOV:",
    highest_month,
    round(highest_aov, 2)
)

print(
    "Lowest Monthly AOV:",
    lowest_month,
    round(lowest_aov, 2)
)

print("\nAnalysis completed successfully!")
