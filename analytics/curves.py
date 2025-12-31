import numpy as np
import pandas as pd
from typing import List, Union

def calculate_zero_rates_bootstrap(
    coupons: Union[List[float], np.ndarray], 
    maturities: Union[List[float], np.ndarray], 
    principal: float = 100.0
) -> np.ndarray:
    """
    Calculates zero rates using the iterative bootstrapping method.
    Assumes annual coupon payments and par pricing.
    """
    coupons = np.asarray(coupons)
    maturities = np.asarray(maturities)
    n = len(maturities)
    
    zrs = np.zeros(n)
    dfs = np.zeros(n)
    
    for i in range(n):
        coupon_payment = coupons[i] * principal
        
        # Price (100) = Sum(PV of previous coupons) + PV of (Final Coupon + Principal)
        previous_cfs_pv = np.sum(coupon_payment * dfs[:i]) if i > 0 else 0
        
        current_df = (principal - previous_cfs_pv) / (coupon_payment + principal)
        dfs[i] = current_df
        zrs[i] = -np.log(current_df) / maturities[i]
    
    return zrs

def calculate_portfolio_pv01(
    df: pd.DataFrame, 
    rate_move: float = 0.0001
) -> pd.DataFrame:
    """
    Calculates PV01 risk buckets for a portfolio of zero-coupon instruments.
    """
    def get_pv(rate_vec):
        return df['principal'] * np.exp(-rate_vec * df['years_to_maturity'])
    
    pv_base = get_pv(df['coupon_rate'])
    pv_shocked = get_pv(df['coupon_rate'] + rate_move)
    df['pv01'] = pv_shocked - pv_base
    
    # Define standard risk buckets
    bins = [0, 1, 5, 10, 30, 100]
    labels = ['0-1Y', '1-5Y', '5-10Y', '10-30Y', '30Y+']
    df['bucket'] = pd.cut(df['years_to_maturity'], bins=bins, labels=labels)
    
    return df.groupby('bucket', observed=False)['pv01'].sum().reset_index()