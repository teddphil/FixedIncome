"""
Behavioural Modelling (Pipe & Filter)
handle Non-Maturing Deposits (NMDs).

The Logic:
Some deposits have no maturity but stay for years.

The Math: 
You may be asked to apply a "decay rule" (e.g., 10% of the balance leaves every year). You need to code a loop that applies this decay to the cash flow array before discounting it.
"""

import pandas as pd
import numpy as np

def cal_nmd(principal, annual_decay_rate, years=10):

	# 1. Calculate balance at each year
	times = np.arange(0, years+1)
	balances = principal * ((1 - annual_decay_rate) ** times)
	
	# 2. CF (out)
	outflows = -np.diff(balances)
	
	# 3. Create schedule
	schedule = pd.DataFrame(
		{
			'Year': np.arange(1, years+1),
			'Openning_Balance': balances[:-1],
			'Outflow_Amount': outflows,
			'Closing_Balance': balances[1:]
		}
	)
	
	return schedule
	
print(cal_nmd(10000, 0.15))