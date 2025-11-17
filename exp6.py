prices = [100, 50, 30]     
quantities = [2, 1, 3]     
discount_rate = 10         
tax_rate = 5               

subtotal = sum(p * q for p, q in zip(prices, quantities))

after_discount = subtotal * (1 - discount_rate / 100)

final_total = after_discount * (1 + tax_rate / 100)

print("Subtotal:", subtotal)
print("Total after discount and tax:", round(final_total, 2))
