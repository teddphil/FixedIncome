import pandas as pd

def simulate_nii(
    existing_loan_df: pd.DataFrame, 
    new_biz_monthly: float, 
    market_rate: float, 
    horizon_months: int = 12
) -> pd.DataFrame:
    """
    Projects Net Interest Income (NII) considering portfolio runoff and new business.
    """
    projection = []
    portfolio = existing_loan_df.copy()
    
    for month in range(1, horizon_months + 1):
        nii = (portfolio['principal'] * portfolio['rate'] / 12).sum()
        projection.append({'Month': month, 'NII': nii})
        
        # Ageing and runoff
        portfolio['months_to_maturity'] -= 1
        portfolio = portfolio[portfolio['months_to_maturity'] > 0].copy()
        
        # New Business Addition
        new_loan = pd.DataFrame([{
            'id': f'NB_{month}',
            'principal': new_biz_monthly,
            'rate': market_rate,
            'months_to_maturity': 24
        }])
        portfolio = pd.concat([portfolio, new_loan], ignore_index=True)
        
    return pd.DataFrame(projection)

def calculate_basis_risk(
    assets_notional: float, 
    liabilities_notional: float, 
    shock_sonia_bps: float, 
    shock_base_bps: float
) -> dict:
    """
    Calculates the NII impact of divergent index moves (Basis Risk).
    """
    asset_delta = assets_notional * (shock_sonia_bps / 10000)
    lia_delta = liabilities_notional * (shock_base_bps / 10000)
    
    return {
        'Asset_NII_Delta': asset_delta,
        'Liability_Cost_Delta': lia_delta,
        'Net_Impact': asset_delta - lia_delta
    }