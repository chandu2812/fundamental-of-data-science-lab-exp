import pandas as pd
import numpy as np
from scipy import stats

# Load dataset (assume file contains a column "rating")
df = pd.read_csv("customer_reviews.csv")
ratings = df["rating"].dropna()

# User input
confidence = float(input("Enter confidence level (e.g., 0.95): "))

# Basic statistics
n = len(ratings)
sample_mean = ratings.mean()
sample_std = ratings.std(ddof=1)

# Confidence interval
alpha = 1 - confidence
t_crit = stats.t.ppf(1 - alpha/2, df=n - 1)
margin_error = t_crit * (sample_std / np.sqrt(n))

lower = sample_mean - margin_error
upper = sample_mean + margin_error

print("\n--- Rating Analysis ---")
print(f"Sample Size: {n}")
print(f"Average Rating: {sample_mean:.3f}")
print(f"{confidence*100:.0f}% Confidence Interval: ({lower:.3f}, {upper:.3f})")
print(f"Margin of Error: ±{margin_error:.3f}")