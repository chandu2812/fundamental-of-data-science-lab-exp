import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load the dataset
data = pd.read_csv("customers.csv")

# 2. Select features for clustering
#    Change these column names based on your dataset
features = data[["age", "annual_income", "spending_score"]]

# 3. Scale the data (important for clustering)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 4. Apply K-Means clustering
k = 4  # number of clusters (you can change this)
kmeans = KMeans(n_clusters=k, random_state=42)
data["cluster"] = kmeans.fit_predict(scaled_features)

# 5. See some results
print("First 10 customers with their clusters:")
print(data[["customer_id", "age", "annual_income", "spending_score", "cluster"]].head(10))

print("\nCluster-wise average values:")
print(data.groupby("cluster")[["age", "annual_income", "spending_score"]].mean())
