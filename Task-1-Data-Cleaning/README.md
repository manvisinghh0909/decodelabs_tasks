# Task 1 - Data Cleaning

This project is about cleaning a messy e-commerce dataset using Python and Pandas.

## What's in this folder
- data_cleaning.py - the script that cleans the data
- data/raw_dataset.xlsx - the original messy dataset
- data/cleaned_dataset.xlsx - the final cleaned dataset

## What I did

The original dataset had 1200 rows and some issues:

- 309 rows had no coupon code, so I filled them with "No Coupon"
- Price columns had messy decimal values, so I rounded them to 2 decimal places
- Dates were in inconsistent formats, so I converted all of them to YYYY-MM-DD
- Some text columns had extra spaces, so I removed them
- I checked if TotalPrice actually matched Quantity x UnitPrice
- I checked for duplicate rows (there were none)

I also added a new column called Discount Applied (Yes/No) to show whether a coupon was used on that order or not.

## Tools used
Python, Pandas, openpyxl

## Result
A clean dataset with 1200 rows and 15 columns, no missing values, no duplicates, and correct numbers.
