import pandas as pd

property_data = pd.DataFrame({
    "property_id": [1, 2, 3, 4, 5],
    "location": ["North", "South", "East", "North", "South"],
    "bedrooms": [3, 5, 4, 6, 2],
    "area_sqft": [1500, 2200, 1800, 2600, 1400],
    "listing_price": [250000, 420000, 310000, 520000, 200000]
})

avg_price_by_location = property_data.groupby("location")["listing_price"].mean()

count_bedrooms_gt4 = property_data[property_data["bedrooms"] > 4].shape[0]

largest_area_property = property_data.loc[property_data["area_sqft"].idxmax()]

print("Average listing price by location:\n", avg_price_by_location, "\n")
print("Number of properties with more than 4 bedrooms:", count_bedrooms_gt4, "\n")
print("Property with the largest area:\n", largest_area_property)
