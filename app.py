from utils import load_data, calculate_risk_return
from topsis import topsis_rank
import pandas as pd

# --- Step 1: Load data ---
sp500, esg = load_data("data/sp500.csv", "data/esg_scores.csv")
merged = pd.merge(sp500, esg, on="Symbol")

# --- Step 2: Calculate risk & return ---
merged = calculate_risk_return(merged)

# --- Step 3: Prepare data for TOPSIS ---
criteria = merged[['Return', 'Risk', 'ESG']]
weights = [0.4, 0.3, 0.3]
impacts = ['+', '-', '+']

# --- Step 4: Rank using TOPSIS ---
merged['Rank'] = topsis_rank(criteria, weights, impacts)
merged = merged.sort_values(by='Rank', ascending=False)

# --- Step 5: Recommend investments ---
target = float(input("🎯 Enter your return goal (e.g. 0.15 for 15%): "))
recommended = merged[merged['Return'] >= target]
print("\n📈 Top Recommended Stocks to Achieve Target Return:\n")
print(recommended[['Symbol', 'Company', 'Return', 'Risk', 'ESG', 'Rank']].head(10))
