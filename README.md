# Bluestock Mutual Fund Analytics

A data analytics project exploring the Indian mutual fund industry — fund performance, NAV trends, investor transactions, SIP growth, AUM, and risk metrics — through an end-to-end pipeline built with Python, SQLite, and Power BI.

---

## Overview

This project takes raw mutual fund data through a complete analytics workflow: ingestion, cleaning, database design, exploratory analysis, performance and risk scoring, and finally an interactive Power BI dashboard for business insights.

```
Raw Data → Data Ingestion → Cleaning & Validation → SQLite Database
   → EDA & Statistical Analysis → Performance & Risk Analytics
   → Power BI Dashboard → Business Insights
```

## Objectives

- Build a clean and reliable mutual fund dataset
- Create a structured relational database using SQLite
- Analyse NAV and fund performance trends
- Compare mutual funds using return and risk metrics
- Analyse investor transaction behaviour
- Study SIP growth and mutual fund industry trends
- Build an interactive Power BI dashboard
- Present findings through a final report and presentation

## Data Sources

| Source | Data Used |
|---|---|
| AMFI India | NAV, AUM, folios and SIP/industry statistics |
| mfapi.in | Historical mutual fund NAV data |
| mfdata.in | NAV and expense-ratio related data |
| NSE India | Benchmark index prices |
| BSE India | BSE SmallCap index data |
| AMFI Monthly Notes | SIP and industry flow statistics |

No proprietary or confidential data is used in the project.

## Dataset Overview

| Dataset | Approx. Records | Description |
|---|---|---|
| `fund_master.csv` | 40 | Mutual fund scheme master data |
| `nav_history.csv` | ~46,000 | Daily NAV history |
| `aum_by_fund_house.csv` | ~90 | Quarterly AUM by fund house |
| `monthly_sip_inflows.csv` | 48 | Monthly SIP industry data |
| `category_inflows.csv` | ~144 | Category-wise net inflows |
| `industry_folio_count.csv` | 21 | Industry folio statistics |
| `scheme_performance.csv` | 40 | Fund performance and risk metrics |
| `investor_transactions.csv` | ~32,778 | Investor transaction records |
| `benchmark_data.csv` | ~8,050 | Benchmark index observations |

NAV data covers roughly January 2022 – May 2026; SIP/industry trend analysis primarily covers 2022–2025.

## Tech Stack

**Programming & Analysis:** Python 3.10+, Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly
**Database:** SQLite, SQLAlchemy
**Dashboard:** Microsoft Power BI
**Dev & Version Control:** Jupyter Notebook, VS Code, Git, GitHub
**Reporting:** ReportLab, PowerPoint

## Database

A SQLite database provides the structured analytical layer, with four main tables:

- **`dim_fund`** — fund reference data (AMFI code, fund house, scheme name, category, plan, risk info)
- **`fact_nav`** — historical NAV observations and calculated daily returns
- **`fact_transactions`** — investor transaction-level data (type, amount, investor attributes, location)
- **`fact_performance`** — fund-level performance and risk metrics

## Analytics Performed

**Exploratory Data Analysis** covering NAV movement, fund-house and category distribution, AUM trends, SIP and folio growth, investor demographics (age group, city tier, payment mode, KYC status), and the risk-return relationship.

**Performance & Risk Analytics** using:
- 3-Year CAGR
- Sharpe Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Expense Ratio
- Composite Fund Score (combines return, risk-adjusted performance, alpha, expense ratio, and drawdown into a comparative ranking)

## Power BI Dashboard

The dashboard (`dashboard/bluestock.pbix`) has four pages:

1. **Industry Overview** — AUM, SIP inflows, folios, scheme count, industry AUM trend, AUM by fund house
2. **Fund Performance** — return vs. risk, fund scorecard, NAV trends, benchmark comparison, fund-house/category/plan filters
3. **Investor Analytics** — transaction type distribution, age-group analysis, monthly transaction trends, state/city-tier analysis, SIP behaviour, KYC status, payment-mode analysis
4. **SIP & Market Trends** — monthly SIP inflows, SIP account growth, NIFTY 50 movement, category-wise inflows, top categories by net inflow, industry trends over time

It also includes slicers, drill-through functionality, a custom tooltip page, and fund-level detail analysis, built with a branded Bluestock theme.

## Key Findings

- SIP inflows increased substantially during the analysed period, with strong growth in active SIP accounts
- Mutual fund folios increased consistently across the industry
- SIP transactions represented the largest share of investor transactions
- The 26–35 age group contributed the highest number of transactions
- T30 investors accounted for a larger share of transactions than B30 investors
- KYC verification levels were high across the analysed investor dataset
- Fund performance varied significantly across categories and risk levels
- Higher returns were not always associated with lower drawdowns
- Risk-adjusted measures like Sharpe Ratio and Maximum Drawdown add useful context beyond return alone

## Project Structure

```
Mutual-Fund-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA
│   └── Performance Analytics
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock.pbix
│
├── screenshots/
│   ├── Page_1_Industry_Overview.png
│   ├── Page_2_Fund_Performance.png
│   ├── Page_3_Investor_Analytics.png
│   └── Page_4_SIP_Market_Trends.png
│
├── reports/
│   └── bluestock.pdf
│
├── outputs/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── run_pipeline.py
├── data_dictionary.md
├── requirements.txt
└── README.md
```

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/Sadiyashaikh15/Mutual-Fund-Analysis.git
cd Mutual-Fund-Analysis
```

**2. Create a virtual environment (Windows)**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the Project

Run the full pipeline end to end:
```bash
python run_pipeline.py
```

Or run individual steps:
```bash
python data_ingestion.py
python live_nav_fetch.py
```

Notebooks (EDA and Performance Analytics) can be opened via Jupyter:
```bash
jupyter notebook
```
or through VS Code.

## Opening the Dashboard

Open `dashboard/bluestock.pbix` in **Microsoft Power BI Desktop** to explore all four dashboard pages, including drill-through and tooltip functionality.

## Deliverables

- `Final_Report.pdf`
- `Bluestock_MF_Presentation.pptx`
- Power BI dashboard (`bluestock.pbix`)
- Python ETL and analytics scripts
- SQL schema and analytical queries
- Data dictionary (`data_dictionary.md`)
- Dashboard screenshots
- Project README

## Limitations

- The analysis is based on the available project datasets and selected mutual fund schemes
- Historical performance does not guarantee future returns
- Some industry-level and fund-level metrics represent different data scopes and shouldn't be treated as identical measures
- Live NAV retrieval depends on API availability
- Power BI Desktop is required to open and interact with the `.pbix` dashboard
- The investor transaction dataset is a provided analytical sample, not a complete representation of all Indian mutual fund investors

## Future Enhancements

- Automated daily NAV updates
- Scheduled ETL execution
- Cloud database integration
- Power BI Service deployment
- Real-time market and benchmark updates
- Automated fund recommendation engine
- Additional portfolio-level risk analytics
- More granular investor segmentation
- Automated dashboard refresh

## Author

**Sadiya Shaikh**
Data Analyst Intern — Bluestock Fintech
GitHub: [Sadiyashaikh15](https://github.com/Sadiyashaikh15)
