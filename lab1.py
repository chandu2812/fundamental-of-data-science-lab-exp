import matplotlib.pyplot as plt
import numpy as np

cars= ['BMW', 'toyota', 'tata', 'maruthi']
sales = [400, 350, 300, 450]

plt.bar(cars, sales)
plt.title('cars Sales')
plt.xlabel('cars')
plt.ylabel('Sales')
plt.show()