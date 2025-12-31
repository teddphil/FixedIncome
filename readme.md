# Fixed Income Analytics & ALM Toolkit

A Python library for Fixed Income analytics, Asset-Liability Management (ALM), and Banking Risk simulation. Designed for quantitative researchers and risk managers.

## Features

### 1. Interest Rate Modelling
Bootstrapping
: Generate zero-rate curves from market bond prices.
Risk Bucketing (PV01)
: Vectorised sensitivity analysis using `pandas` categories for maturity buckets (1Y, 5Y, 10Y+).

### 2. Behavioural Analytics
Prepayment Engines
: Model loan schedules using CPR (Conditional Prepayment Rate) and SMM (Single Monthly Mortality) logic.
NMD Decay
: Simulate the outflow profiles of Non-Maturing Deposits using exponential decay functions.

### 3. Balance Sheet Risk
Dynamic NII Projection
: Simulate a 12-month Net Interest Income horizon including portfolio runoff and new business reinvestment.
Basis Risk Analysis
: Quantify the impact of divergent interest rate shocks (e.g., SONIA vs. Bank of England Base Rate).