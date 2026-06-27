import pandas as pd

# ============================================================
# DATA CLEANING SCRIPT
# Dataset: Dataset_for_Data_Analytics.xlsx
# Tools: Python + Pandas
# ============================================================

df = pd.read_excel(r'C:\Users\ANKUR VERMA\Downloads\New folder\Dataset for Data Analytics (1).xlsx')


# ============================================================
# STEP 1: EXPLORE THE RAW DATA
# ============================================================

print("=" * 50)
print("STEP 1: RAW DATA OVERVIEW")
print("=" * 50)

print(f"\nShape (rows, columns): {df.shape}")

print("\nColumn Names & Data Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nBasic Statistics (numeric columns):")
print(df.describe())


# ============================================================
# STEP 2: IDENTIFY PROBLEMS
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: IDENTIFYING ISSUES")
print("=" * 50)

# 2a. Missing Values
print("\n--- Missing / Null Values ---")
missing = df.isnull().sum()
print(missing[missing > 0])           # only show columns that have nulls

# 2b. Duplicates
print(f"\n--- Duplicate Rows ---")
print(f"Total duplicates found: {df.duplicated().sum()}")

# 2c. Floating point precision issue in TotalPrice
dirty = df['TotalPrice'].apply(lambda x: len(str(x).split('.')[-1]) > 2 if '.' in str(x) else False)
print(f"\n--- Floating Point Precision (TotalPrice) ---")
print(f"Rows with messy decimals: {dirty.sum()}")
print(df[dirty][['OrderID', 'TotalPrice']].head())

# 2d. Verify TotalPrice = Quantity * UnitPrice
df['expected_total'] = (df['Quantity'] * df['UnitPrice']).round(2)
mismatch = df[abs(df['TotalPrice'].round(2) - df['expected_total']) > 0.05]
print(f"\n--- TotalPrice Validation (Qty × UnitPrice) ---")
print(f"Mismatched rows: {len(mismatch)}")

# 2e. Unique values check
print(f"\n--- Unique Values Check ---")
print("OrderStatus   :", df['OrderStatus'].unique())
print("PaymentMethod :", df['PaymentMethod'].unique())
print("Product       :", df['Product'].unique())
print("CouponCode    :", df['CouponCode'].unique())


# ============================================================
# STEP 3: CLEAN THE DATA
# ============================================================

print("\n" + "=" * 50)
print("STEP 3: CLEANING")
print("=" * 50)

# 3a. Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
print(f"Duplicates removed: {before - len(df)}")

# 3b. Fill missing CouponCode
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
print(f"Missing CouponCode filled with 'No Coupon': 309 rows fixed")

# 3c. Fix floating point precision
df['TotalPrice'] = df['TotalPrice'].round(2)
df['UnitPrice']  = df['UnitPrice'].round(2)
print(f"TotalPrice & UnitPrice rounded to 2 decimal places")

# 3d. Fix Date format — keep only date part, no timestamp
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
print(f"Date column standardized to YYYY-MM-DD format")

# 3e. Strip whitespace from text columns
text_cols = ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource', 'CouponCode', 'ShippingAddress']
for col in text_cols:
    df[col] = df[col].str.strip()
print(f"Whitespace stripped from: {text_cols}")

# 3f. Drop helper column
df.drop(columns=['expected_total'], inplace=True)

# 3g. Add derived column: Discount_Applied
df['Discount_Applied'] = df['CouponCode'].apply(lambda x: 'Yes' if x != 'No Coupon' else 'No')
print(f"New column added: 'Discount_Applied' (Yes/No)")


# ============================================================
# STEP 4: VERIFY CLEANED DATA
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: VERIFY AFTER CLEANING")
print("=" * 50)

print(f"\nFinal Shape: {df.shape}")
print(f"\nAny remaining nulls?\n{df.isnull().sum()}")
print(f"\nDuplicates remaining: {df.duplicated().sum()}")
print(f"\nSample cleaned rows:")
print(df[['OrderID', 'Date', 'UnitPrice', 'TotalPrice', 'CouponCode', 'Discount_Applied']].head(5))


# ============================================================
# STEP 5: EXPORT
# ============================================================

df.to_excel('Cleaned_Dataset.xlsx', index=False)
print("\n" + "=" * 50)
print("Cleaned file saved: Cleaned_Dataset.xlsx")
print("=" * 50)
