"""
The "Risk Bucketing" Task

The Problem

You are given a CSV of 10,000 trades with columns trade_id, notional, rate, and maturity_date. The Goal: Write a function to calculate the total PV01 for each of the following buckets: 0-1yr, 1-5yr, 5-10yr, and 10yr+.

Key skill

Use pd.cut() and np.exp() to vectorise the calculation for all 10,000 rows at once.
"""

import pandas as pd
import numpy as np

def calculate_pv01(df, rate_move = 0.0001):

	# calculate pv01
	def calculate_pv(rate):
		return df['principal'] * np.exp(-rate * df['years_to_maturity'])
	
	pv_before = calculate_pv(df['coupon_rate'])
	pv_after = calculate_pv(df['coupon_rate'] + rate_move)
	df['pv01'] = pv_after - pv_before
	
	# Aggregate
	bins = [0,1,5,10,30,100]
	labs = ['0-1','1-5','5-10','10-30','30+']
	df['bucket'] = pd.cut(df['years_to_maturity'], bins=bins, labels=labs)
	
	risk_report = df.groupby('bucket')['pv01'].sum().reset_index()
	
	return risk_report
	
data = {
	'principal':[100,500,2000],
	'coupon_rate':[0.04,0.03,0.05],
	'years_to_maturity':[0.5,3.5,12]
}

df_portfolio = pd.DataFrame(data)
print(calculate_pv01(df_portfolio))