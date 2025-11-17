#Line Plot of Monthly Sales Data
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 200, 210]

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Plot")
plt.grid(True)
plt.tight_layout()
plt.show()
#2. Bar Plot of Monthly Sales Data
import matplotlib.pyplot as plt

# Sample monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 200, 210]

# Bar plot
plt.figure(figsize=(8, 4))
plt.bar(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Bar Plot")
plt.tight_layout()
plt.show()
