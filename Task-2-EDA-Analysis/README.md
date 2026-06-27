# Task 2 - Basic Statistics & EDA

This project is about exploring an e-commerce orders dataset and finding out basic statistics, trends, and patterns in it using Python and Pandas.

## What's in this folder
- basic_statistics.py - the script that does the analysis
- Dataset_for_Data_Analytics.xlsx - the dataset used
- EDA_Report.xlsx - the final report with all findings (summary, statistics, trends, distributions)

## What I did

The dataset has 1200 orders from Jan 2023 to Jun 2025, with 14 columns.

In the script, I calculated:
- Basic info like row/column count, data types, missing values
- Mean, median, mode, standard deviation, variance, min, max and range for all numeric columns
- Percentiles (25th, 50th, 75th, 90th)
- Skewness and kurtosis (to check how the data is distributed)
- Value counts for categorical columns like Product, Order Status, Payment Method, Referral Source
- Correlation between numeric columns

## Key findings

- Total Revenue: ₹12,64,762 from 1,200 orders, average order value ₹1,054
- Revenue peaked in June 2024 (₹68,069) and was lowest in April 2023 (₹27,752); overall trend is slightly declining after 2023
- Printer is the most ordered product (181 orders), but Laptop has the highest average order value (₹1,111)
- Almost 50% of orders are Cancelled or Returned, which is a concern worth looking into
- Found 8 high-value outliers in TotalPrice, all with Quantity = 5
- CouponCode column had 309 missing values (about 26%) - likely orders where no coupon was used
- Instagram is the top referral source (259 orders), followed closely by Email (250)
- Online payment is the most used payment method, but all 5 payment methods are fairly evenly used

## Tools used
Python, Pandas, NumPy, SciPy

## Result
A complete statistical summary of the dataset along with an EDA report covering revenue trends, product performance, order status breakdown, and other key business insights.
