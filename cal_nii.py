"""
Dynamic NII tests.

The Task:

You are given a portfolio and a "New Business" forecast (e.g., "we will issue £100m of new 2Y loans every month").

The Challenge:

You must model how the total NII changes over a 12-month horizon as old loans mature and new loans are added at current market rates.
"""
import pandas as pd
import numpy as np

def calculate_nii(existing_loan, new_business_monthly, market_rate):
	"""
	existing_loan: data frame ['id', 'principal', 'rate', 'months_to_maturity']
	new_business_monthly: float, amount of new loans issued each month
	market rate: float, interest rate for new loans
	"""
	nii_projection = []
	portfolio_current = existing_loan.copy()
	
	# monthly simulation
	for month in range(1,13):
		nii_monthly = (portfolio_current['principal'] * portfolio_current['rate']/12).sum()
		nii_projection.append({'Month': month, 'NII':nii_monthly})
		portfolio_current['months_to_maturity'] -= 1
		portfolio_current = portfolio_current[portfolio_current['months_to_maturity']>0]
		loan_new = pd.DataFrame(
			[
				{
					'id': f'new_{month}',
					'principal': new_business_monthly,
					'rate': market_rate,
					'months_to_maturity': 24
				}
			]
		)
		portfolio_current = pd.concat(
			[
				portfolio_current,
				loan_new
			],
			ignore_index=True
		)
	return pd.DataFrame(nii_projection)
	
# Example Usage
initial_assets = pd.DataFrame([
    {'id': 'L1', 'principal': 1000000, 'rate': 0.05, 'months_to_maturity': 3},
    {'id': 'L2', 'principal': 2000000, 'rate': 0.04, 'months_to_maturity': 10}
])

report = calculate_nii(initial_assets, new_business_monthly=500000, market_rate=0.06)
print(report)
		