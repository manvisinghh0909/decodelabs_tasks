# ============================================================
#   Basic Statistics using Pandas
#   Dataset: E-Commerce Orders
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats

# ── 1. Load Dataset ──────────────────────────────────────────
df = pd.read_excel('Dataset_for_Data_Analytics__2_.xlsx')

print("=" * 55)
print("       BASIC STATISTICS USING PANDAS")
print("=" * 55)

# ── 2. Dataset Overview ──────────────────────────────────────
print("\n📌 DATASET OVERVIEW")
print("-" * 40)
print(f"  Total Rows    : {df.shape[0]}")
print(f"  Total Columns : {df.shape[1]}")
print(f"  Column Names  : {list(df.columns)}")

# ── 3. First 5 Rows ──────────────────────────────────────────
print("\n📌 FIRST 5 ROWS (df.head())")
print("-" * 40)
print(df.head())

# ── 4. Data Types & Null Check ───────────────────────────────
print("\n📌 DATA TYPES (df.dtypes)")
print("-" * 40)
print(df.dtypes)

print("\n📌 NULL VALUES (df.isnull().sum())")
print("-" * 40)
print(df.isnull().sum())

# ── 5. describe() — Summary Statistics ───────────────────────
print("\n📌 SUMMARY STATISTICS (df.describe())")
print("-" * 40)
print(df.describe())

# ── 6. Mean ──────────────────────────────────────────────────
print("\n📌 MEAN  (df.mean())")
print("-" * 40)
numeric_df = df.select_dtypes(include='number')
print(numeric_df.mean())

# ── 7. Median ────────────────────────────────────────────────
print("\n📌 MEDIAN  (df.median())")
print("-" * 40)
print(numeric_df.median())

# ── 8. Mode ──────────────────────────────────────────────────
print("\n📌 MODE  (df.mode())")
print("-" * 40)
print(df.mode().iloc[0])          # mode() returns DataFrame; row 0 = first mode

# ── 9. Standard Deviation & Variance ─────────────────────────
print("\n📌 STANDARD DEVIATION  (df.std())")
print("-" * 40)
print(numeric_df.std())

print("\n📌 VARIANCE  (df.var())")
print("-" * 40)
print(numeric_df.var())

# ── 10. Min & Max ─────────────────────────────────────────────
print("\n📌 MINIMUM  (df.min())")
print("-" * 40)
print(numeric_df.min())

print("\n📌 MAXIMUM  (df.max())")
print("-" * 40)
print(numeric_df.max())

# ── 11. Range ────────────────────────────────────────────────
print("\n📌 RANGE  (max - min)")
print("-" * 40)
print(numeric_df.max() - numeric_df.min())

# ── 12. Percentiles / Quantiles ──────────────────────────────
print("\n📌 PERCENTILES  (25th, 50th, 75th, 90th)")
print("-" * 40)
print(numeric_df.quantile([0.25, 0.50, 0.75, 0.90]))

# ── 13. Skewness & Kurtosis ──────────────────────────────────
print("\n📌 SKEWNESS  (df.skew())")
print("-" * 40)
print(numeric_df.skew())

print("\n📌 KURTOSIS  (df.kurtosis())")
print("-" * 40)
print(numeric_df.kurtosis())

# ── 14. Value Counts (Categorical Columns) ───────────────────
cat_cols = ['Product', 'OrderStatus', 'PaymentMethod', 'ReferralSource']

for col in cat_cols:
    print(f"\n📌 VALUE COUNTS — {col}")
    print("-" * 40)
    print(df[col].value_counts())

# ── 15. Correlation Matrix ───────────────────────────────────
print("\n📌 CORRELATION MATRIX  (df.corr())")
print("-" * 40)
print(numeric_df.corr().round(2))

# ── 16. Column-wise Stats (Custom Summary Table) ─────────────
print("\n📌 CUSTOM SUMMARY TABLE")
print("-" * 55)
print(f"{'Column':<14} {'Mean':>9} {'Median':>9} {'Mode':>9} {'Std':>9} {'Min':>7} {'Max':>9}")
print("-" * 55)
for col in numeric_df.columns:
    m  = df[col].mean()
    md = df[col].median()
    mo = stats.mode(df[col], keepdims=True).mode[0]
    sd = df[col].std()
    mn = df[col].min()
    mx = df[col].max()
    print(f"{col:<14} {m:>9.2f} {md:>9.2f} {mo:>9.2f} {sd:>9.2f} {mn:>7.2f} {mx:>9.2f}")

print("\n✅ Basic Statistics Complete!")
