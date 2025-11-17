import pandas as pd

sales_data = pd.DataFrame({
    "product_name": ["A", "B", "A", "C", "B", "D", "A", "E", "B", "C"],
    "quantity": [10, 5, 7, 3, 12, 8, 4, 2, 1, 6],
    "sale_date": [
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-04", "2024-01-05", "2024-01-06",
        "2024-01-07", "2024-01-08", "2024-01-09", "2024-01-10"
    ]
})

sales_data["sale_date"] = pd.to_datetime(sales_data["sale_date"])

product_totals = sales_data.groupby("product_name")["quantity"].sum()

top_5_products = product_totals.sort_values(ascending=False).head(5)

print("Top 5 most sold products:")
print(top_5_products)
