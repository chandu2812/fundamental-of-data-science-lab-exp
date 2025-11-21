import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [10, 12, 15, 20, 25, 30, 32, 31, 28, 22, 16, 11] # Celsius
rainfall = [50, 40, 60, 80, 100, 120, 150, 140, 110, 90, 70, 55] # mm

# 1. Line Plot for Monthly Temperature
plt.figure(figsize=(10, 5))
plt.plot(months, temperature, marker='o', color='orange', linestyle='-', linewidth=2)
plt.title('Monthly Temperature Trend')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# 2. Scatter Plot for Monthly Rainfall
plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall, color='blue', s=100, alpha=0.6) # s is marker size
plt.title('Monthly Rainfall Distribution')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
