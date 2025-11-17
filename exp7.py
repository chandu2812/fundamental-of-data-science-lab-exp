import pandas as pd

order_data = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 101],
    "order_date": ["2024-01-05", "2024-01-07", "2024-01-10",
                   "2024-01-02", "2024-01-12", "2024-01-15"],
    "product_name": ["Laptop", "Mouse", "Laptop", "Keyboard", "Laptop", "Mouse"],
    "order_quantity": [1, 2, 1, 3, 2, 1]
})

order_data["order_date"] = pd.to_datetime(order_data["order_date"])

total_orders = order_data.groupby("customer_id").size()

avg_quantity = order_data.groupby("product_name")["order_quantity"].mean()

earliest_date = order_data["order_date"].min()
latest_date = order_data["order_date"].max()

print("Total orders by each customer:")
print(total_orders, "\n")

print("Average order quantity for each product:")
print(avg_quantity, "\n")

print("Earliest order date:", earliest_date.date())
print("Latest order date:", latest_date.date())
