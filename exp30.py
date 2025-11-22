import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

# --------------------------------------------------
# 1. Example dataset (replace with your real data)
# Features: [mileage_km, age_years, brand_code, engine_type_code]
# Target: price in lakhs (example values)
#
# Brand encoding: 1 = Maruti, 2 = Hyundai, 3 = Toyota
# Engine encoding: 1 = Petrol, 2 = Diesel
# --------------------------------------------------
X = np.array([
    [30000, 3, 1, 1],
    [50000, 5, 1, 2],
    [20000, 2, 2, 1],
    [70000, 7, 2, 2],
    [15000, 1, 3, 1],
    [60000, 6, 3, 2],
    [40000, 4, 2, 1],
    [80000, 8, 1, 2]
])

y = np.array([5.5, 4.0, 7.0, 3.5, 9.0, 4.5, 6.0, 3.0])

feature_names = ["mileage_km", "age_years", "brand_code", "engine_type_code"]

# --------------------------------------------------
# 2. Train CART (Decision Tree Regressor)
# --------------------------------------------------
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# --------------------------------------------------
# 3. User input for new car
# --------------------------------------------------
print("Enter details of the car you want to sell:")

mileage = float(input("Mileage (in km): "))
age = float(input("Age (in years): "))

print("\nBrand codes: 1 = Maruti, 2 = Hyundai, 3 = Toyota")
brand = int(input("Brand code: "))

print("\nEngine type codes: 1 = Petrol, 2 = Diesel")
engine = int(input("Engine type code: "))

new_car = np.array([[mileage, age, brand, engine]])

# --------------------------------------------------
# 4. Predict price
# --------------------------------------------------
predicted_price = model.predict(new_car)[0]
print("\n--- Prediction ---")
print(f"Predicted price: {predicted_price:.2f} lakhs")

# --------------------------------------------------
# 5. Display decision path
# --------------------------------------------------
tree_ = model.tree_

node_indicator = model.decision_path(new_car)
leaf_id = model.apply(new_car)[0]

print("\n--- Decision Path ---")

# indices of the nodes for this sample
node_index = node_indicator.indices[node_indicator.indptr[0] : node_indicator.indptr[1]]

for node_id in node_index:
    # Skip leaf node
    if node_id == leaf_id:
        continue

    feature_index = tree_.feature[node_id]
    threshold = tree_.threshold[node_id]

    if new_car[0, feature_index] <= threshold:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    feat_name = feature_names[feature_index]
    feat_value = new_car[0, feature_index]

    print(f"If ({feat_name} = {feat_value:.2f}) {threshold_sign} {threshold:.2f}")

print(f"\nReached leaf node: {leaf_id}, predicted price = {predicted_price:.2f} lakhs")
