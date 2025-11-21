import pandas as pd

# 1. Setup Mock Data (assuming this structure based on prompt)
data = {
    'customer_id': [101, 102, 103, 104, 105, 106],
    'age': [25, 34, 25, 45, 34, 60]
}
df = pd.DataFrame(data)

# 2. Calculate Frequency
# .sort_index() is crucial here. Without it, Pandas sorts by the count (high to low),
# which makes the age trend impossible to read.
age_counts = df['age'].value_counts().sort_index()

print("Age Frequency Distribution:")
print(age_counts)