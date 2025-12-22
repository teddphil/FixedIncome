"""
The "Yield Curve Bootstrapping" Task

The Problem:

You are given market prices for a series of bonds with different maturities. The Goal: Write a function to solve for the Zero Rates (rt​) iteratively.

Key skill:

Using a root-finding algorithm (like scipy.optimize.newton) or an iterative loop that correctly identifies the next discount factor DF(t) based on previous results.
"""

import numpy as np

def calculate_zero_rates_bootstrap(coupons, maturities, principal = 100):

	"""
	coupons: list, annual coupon rates
	maturities: list, years
	returns: array, zero rates
	
	Abbreviations:
		ZR: zero rate
		DF: discount factor
		CF: cash flow
		PV: present value
	"""
	
	ZRs = np.zeros(len(maturities))
	DFs = np.zeros(len(maturities))
	
	for i in range(len(maturities)):
		price = principal
		coupon_payment = coupons[i] * principal
		
		if i==0:
				previous_CFs_PV = 0
		else:
				previous_CFs_PV = np.sum(coupon_payment * DFs[:i])
				
		# Price = Sum of PVs of Previous Coupons + (Final Coupon + Principal) × Current DF
		
		DF_current = (price - previous_CFs_PV) / (coupon_payment + principal)
		
		DFs[i] = DF_current
		
		ZRs[i] = -np.log(DF_current) / maturities[i]
	
	return ZRs
	
rates = calculate_zero_rates_bootstrap([0.02, 0.03, 0.04], [1, 2, 3])
print(f"Zero rates: {rates}")
	
			
		