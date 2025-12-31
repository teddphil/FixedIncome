"""
The "Cash Flow Engine" Task

The Problem: 

Given a loan with a specific principal, interest rate, and a CPR (Conditional Prepayment Rate).

The Goal: 

Generate the monthly cash flow schedule, accounting for interest, scheduled principal, and prepayments.

Key skill: 

Correctly applying the SMM=1−(1−CPR)1/12 formula to adjust the remaining principal each month.
"""

import numpy as np
import pandas as pd

def calculate_prepayment_schedule(principal, annual_rate, tenure_month, CPR):
	"""
	Abbreviations:
		CPR: Conditional Prepayment Rate
		SMM: Single Monthly Mortality
		MR:  Monthly Rate
	"""
	MR = annual_rate / 12
	SMM = 1 - (1-CPR)**(1/12)
	
	# Fixed monthly payment
	# P * r * (1+r)^n / ((1+r)^n - 1)
	repayment = principal * (MR * (1+MR)**tenure_month) / ((1+MR)**tenure_month - 1)
	
	balance_remain = principal
	schedule = []
	
	for month in range(1, tenure_month + 1):
		interest_comp = balance_remain * MR
		principal_scheduled = min(repayment-interest_comp, balance_remain)
		balance_after_scheduled = balance_remain - principal_scheduled
		prepayment = balance_after_scheduled * SMM
		principal_total = principal_scheduled + prepayment
		CF_total = interest_comp + principal_total
		
		schedule.append({
			'Month': month,
			'Opening_Balance': balance_remain,
			'Interest': interest_comp,
			'Scheduled_Principal': principal_scheduled,
			'Prepayment': prepayment,
			'Total_CF': CF_total,
			'Closing_Balance': balance_remain - principal_total
		})
		
		balance_remain -= principal_total
		if balance_remain<=0: break
		
	return pd.DataFrame(schedule)
	
df = calculate_prepayment_schedule(1000000, 0.05, 360, 0.10)
print(df)