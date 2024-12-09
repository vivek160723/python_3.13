from inventory.product import Product

product = Product(name="Laptop", price=75000, quantity=10)

print("Initial Product Details:")
print(product)

    # Update the quantity
product.update_quantity(12)
print("\nAfter Updating Quantity:")
print(product)

    # Calculate total value
total_value = product.calculate_total_value()
print(f"\nTotal Value of Stock: ₹{total_value}")

