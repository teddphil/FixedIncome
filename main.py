from analytics.curves import calculate_portfolio_pv01
from analytics.lending import calculate_prepayment_schedule
import pandas as pd

# 1. PV01 Example
data = {
    'principal': [1000000, 5000000, 2000000],
    'coupon_rate': [0.04, 0.035, 0.05],
    'years_to_maturity': [0.5, 4.2, 12.0]
}
portfolio = pd.DataFrame(data)
risk_report = calculate_portfolio_pv01(portfolio)
print("--- Risk Report ---")
print(risk_report)

# 2. Prepayment Example
loan_schedule = calculate_prepayment_schedule(1000000, 0.05, 360, 0.10)
print("\n--- Loan Schedule (First 5 Months) ---")
print(loan_schedule.head())