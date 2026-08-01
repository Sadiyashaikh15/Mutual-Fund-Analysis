# Mutual Fund Analytics - Data Dictionary

## 1. dim_fund

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Scheme Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub-category |
| plan | TEXT | Regular / Direct |
| benchmark | TEXT | Benchmark Index |
| risk_category | TEXT | Risk Classification |

---

## 2. fact_nav

| Column | Data Type | Description |
|---------|----------|-------------|
| nav_id | INTEGER | Unique NAV Record ID |
| amfi_code | INTEGER | Fund Identifier |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## 3. fact_transactions

| Column | Data Type | Description |
|---------|----------|-------------|
| transaction_id | INTEGER | Unique Transaction ID |
| investor_id | TEXT | Investor Identifier |
| amfi_code | INTEGER | Fund Identifier |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | T30 / B30 |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Investor Gender |
| annual_income_lakh | REAL | Annual Income (Lakhs) |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | KYC Status |

---

## 4. fact_performance

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | INTEGER | Fund Identifier |
| return_1yr_pct | REAL | 1-Year Return |
| return_3yr_pct | REAL | 3-Year Return |
| return_5yr_pct | REAL | 5-Year Return |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown |
| expense_ratio_pct | REAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |

---

## Database

SQLite

## Data Source

- AMFI India
- mfapi.in
- Bluestock Capstone Dataset