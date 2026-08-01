SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT
    AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;

SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

SELECT
    amfi_code,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

SELECT
    scheme_name,
    alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

SELECT
    state,
    AVG(amount_inr) AS avg_transaction
FROM fact_transactions
GROUP BY state
ORDER BY avg_transaction DESC;

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode;

SELECT
    city_tier,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY city_tier;