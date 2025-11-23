import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

# Load dataset
data = pd.read_csv("car_data.csv")

# Convert categorical columns to numbers
data["brand"] = data["brand"].astype("category").cat.codes
data["engine_type"] = data["engine_type"].astype("category").cat.codes

# Features and target
X = data[["mileage", "age", "brand", "engine_type"]]
y = data["price"]

# Train CART model
model = DecisionTreeRegressor()
model.fit(X, y)

# Take user input
mileage = float(input("Enter mileage: "))
age = float(input("Enter age: "))
brand = int(input("Enter brand code (check dataset): "))
engine = int(input("Enter engine type code (check dataset): "))

# Predict
new_car = [[mileage, age, brand, engine]]
pred_price = model.predict(new_car)[0]

print("\nPredicted Price:", pred_price)

# Display decision tree path
print("\nDecision Path:")
tree_rules = export_text(model, feature_names=["mileage", "age", "brand", "engine_type"])
print(tree_rules)
