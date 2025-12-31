import numpy as np
import pandas as pd

def calculate_prepayment_schedule(
    principal: float, 
    annual_rate: float, 
    tenure_months: int, 
    cpr: float
) -> pd.DataFrame:
    """
    Generates a monthly repayment schedule accounting for CPR (Conditional Prepayment Rate).
    """
    monthly_rate = annual_rate / 12
    smm = 1 - (1 - cpr)**(1/12)
    
    # Standard Annuity Formula
    periodic_pmt = principal * (monthly_rate * (1 + monthly_rate)**tenure_months) / \
                   ((1 + monthly_rate)**tenure_months - 1)
    
    balance = principal
    records = []
    
    for month in range(1, tenure_months + 1):
        interest = balance * monthly_rate
        sched_principal = min(periodic_pmt - interest, balance)
        
        balance_post_sched = balance - sched_principal
        prepayment = balance_post_sched * smm
        
        total_principal = sched_principal + prepayment
        records.append({
            'Month': month,
            'Opening_Balance': balance,
            'Interest': interest,
            'Prepayment': prepayment,
            'Closing_Balance': balance - total_principal
        })
        
        balance -= total_principal
        if balance <= 1e-6: break
        
    return pd.DataFrame(records)

def calculate_nmd_decay(
    principal: float, 
    annual_decay_rate: float, 
    years: int = 10
) -> pd.DataFrame:
    """
    Models the decay of Non-Maturing Deposits (NMDs).
    """
    times = np.arange(0, years + 1)
    balances = principal * ((1 - annual_decay_rate) ** times)
    outflows = -np.diff(balances)
    
    return pd.DataFrame({
        'Year': np.arange(1, years + 1),
        'Opening_Balance': balances[:-1],
        'Outflow': outflows,
        'Closing_Balance': balances[1:]
    })