import numpy as np
from scipy import stats

# Generate synthetic dataset (1000 measurements)
# You can adjust mean and std based on your scenario
data = np.random.normal(loc=50, scale=10, size=1000)

# User inputs
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g., 0.95): "))
precision = float(input("Enter desired precision (+/- value): "))

# Random sample
sample = np.random.choice(data, n, replace=False)

# Point estimate
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Confidence interval
alpha = 1 - confidence
t_crit = stats.t.ppf(1 - alpha/2, df=n - 1)
margin_error = t_crit * (sample_std / np.sqrt(n))

lower = sample_mean - margin_error
upper = sample_mean + margin_error

print("\n--- Results ---")
print(f"Sample Mean: {sample_mean:.4f}")
print(f"Confidence Interval: ({lower:.4f}, {upper:.4f})")
print(f"Margin of Error: ±{margin_error:.4f}")

# Precision check
if margin_error <= precision:
    print("Precision requirement satisfied.")
else:
    print("Precision requirement NOT satisfied. Increase sample size.")
