# Ecommerce Sales Analysis

## Project Overview

This project analyses ecommerce sales data to understand sales performance, customer behaviour, product performance and areas that may require business attention.

The analysis was performed using Python and focuses on basic data cleaning, exploratory data analysis, visualisation and business insights.

## Dataset

The dataset contains ecommerce order information including:

- Order ID
- Customer ID
- Product ID
- Category
- Price
- Discount
- Quantity
- Payment Method
- Order Date
- Delivery Time
- Region
- Return Status
- Total Amount
- Shipping Cost
- Profit Margin
- Customer Age
- Customer Gender

The dataset contains 34,500 orders and 17 columns.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Spyder

## Data Cleaning

The following basic data cleaning steps were performed:

- Checked missing values
- Checked duplicate records
- Removed duplicate records
- Checked data types
- Converted the order date into datetime format
- Created customer age groups

## Analysis Performed

### Sales Analysis

- Category-wise sales
- Region-wise sales
- Top 10 products by sales
- Monthly sales trend

### Customer Analysis

- Orders by age group
- Sales by age group
- Orders by gender
- Sales by gender
- Average Order Value (AOV)

### Return Analysis

- Overall return percentage
- Return rate by category

### Profit Analysis

- Average profit margin value by category
- Total profit margin value by category
- Sales and profit comparison

### Trend and Correlation Analysis

- Monthly order trend
- Monthly AOV
- Correlation matrix
- Correlation heatmap
- Total amount vs profit margin

## Key Business Insights

1. Electronics was the strongest category in terms of total sales.

2. Grocery had the lowest sales and showed a negative value in the profit_margin field, making it an area that requires further investigation.

3. Fashion had the highest return rate among the categories.

4. South had the highest number of orders among the regions, while Central had the lowest.

5. The 26–35 age group was an important customer segment and generated the highest sales.

6. Female customers contributed the highest total sales and order volume.

7. Male customers had the highest Average Order Value.

8. December 2024 recorded the highest monthly AOV, while August 2024 recorded the lowest.

9. Total amount and profit_margin showed a strong positive correlation in the dataset.

## Business Recommendations

- Investigate the reasons behind the high return rate in Fashion.
- Analyse Grocery products to understand the negative profit_margin values.
- Monitor Electronics inventory and product performance because it is the main sales contributor.
- Study the 26–35 customer segment for targeted marketing opportunities.
- Analyse high-AOV customer segments to understand their purchasing behaviour.
- Further investigate pricing, discounts and shipping costs for categories with weaker profitability.

## Project Structure

Ecommerce-Sales-Analysis/

    data/
        Ecommerce_Sales.csv

    scripts/
        Analysis01.py

    charts/
        category_sales.png
        region_orders.png
        monthly_sales.png
        top_10_products.png
        category_return_rate.png
        category_profit.png
        age_group_sales.png
        gender_sales.png
        correlation_heatmap.png
        sales_vs_profit.png

    README.md

## Conclusion

This project helped me understand how Python can be used to clean ecommerce data, analyse sales and customer behaviour, identify trends and communicate business insights through visualisations.

The analysis also helped identify categories and customer segments that are performing well and areas that require further investigation.