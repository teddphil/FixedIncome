"""
Basis Risk Coding

The Scenario: 

You might have assets linked to SONIA and liabilities linked to the Bank of England Base Rate.

The Task: 

Calculate the impact if SONIA rises by 50bps but Base Rate only rises by 25bps. This tests your ability to map different indices to different products in your Python logic.

"""

import pandas as pd

def cal_basis_risk(notional_assets, notional_liabilities, shock_sonia, shock_base):
	asset_income_change = notional_assets * (shock_sonia/10000)
	liability_cost_change = notional_liabilities * (shock_base/10000)
	net_impact = asset_income_change - liability_cost_change
	impact_metric = {
		'Asset_change': asset_income_change,
		'Liability_change': liability_cost_change,
		'Net_NII_impact': net_impact
	}
	return impact_metric
	
impact = cal_basis_risk(500_000_000, 450_000_000, 50, 25)
print(impact)