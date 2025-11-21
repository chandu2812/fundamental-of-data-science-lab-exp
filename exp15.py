import pandas as pd

# 1. Mock Data (Long Tail Distribution typical in social media)
data = {'post_id': range(1, 11),
        'likes': [0, 2, 1, 500, 2, 1, 0, 10000, 1, 5]} 
df = pd.DataFrame(data)

# 2. The Naive Approach (Exact Counts)
# Good for small ranges, bad for viral posts.
raw_counts = df['likes'].value_counts().sort_index()

# 3. The Professional Approach (Binning)
# Group likes into logical buckets to handle the massive variance.
bins = [0, 10, 100, 1000, float('inf')]
labels = ['Low (0-10)', 'Medium (11-100)', 'High (101-1K)', 'Viral (1K+)']

df['engagement_level'] = pd.cut(df['likes'], bins=bins, labels=labels, right=False)
distribution = df['engagement_level'].value_counts().sort_index()

print("--- Raw Frequency (Noisy) ---")
print(raw_counts)
print("\n--- Binned Frequency (Actionable) ---")
print(distribution)