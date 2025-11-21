import matplotlib.pyplot as plt
import numpy as np

# Sample Data: Days of the month (1-30) and random Sales figures
days = np.arange(1, 31)
sales = np.random.randint(100, 500, size=30)

# 1. Line Plot
plt.figure(figsize=(10, 5))
plt.plot(days, sales, marker='o', linestyle='-', color='blue')
plt.title('Daily Sales Trend (Line Plot)')
plt.xlabel('Day of Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(days, sales, color='red', alpha=0.7)
plt.title('Daily Sales Distribution (Scatter Plot)')
plt.xlabel('Day of Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()

# 3. Bar Plot
plt.figure(figsize=(10, 5))
plt.bar(days, sales, color='green')
plt.title('Daily Sales Volume (Bar Plot)')
plt.xlabel('Day of Month')
plt.ylabel('Sales ($)')
plt.grid(axis='y')
plt.show()