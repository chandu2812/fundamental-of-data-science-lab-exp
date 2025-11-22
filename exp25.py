from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
species = iris.target_names

# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# User input for new flower
print("Enter the flower measurements:")

sepal_length = float(input("Sepal length: "))
sepal_width = float(input("Sepal width: "))
petal_length = float(input("Petal length: "))
petal_width = float(input("Petal width: "))

new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Prediction
prediction = model.predict(new_flower)[0]
predicted_species = species[prediction]

print("\n--- Prediction Result ---")
print(f"The predicted species is: {predicted_species}")