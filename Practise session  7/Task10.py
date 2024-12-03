class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Adds an item to the shopping cart."""
        self.items.append(item)
        print(f"Item '{item}' added to the cart.")

    def remove_item(self, item):
        """Removes an item from the shopping cart."""
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from the cart.")
        else:
            print(f"Item '{item}' not found in the cart.")

    def display_items(self):
        """Displays all the items in the shopping cart."""
        if self.items:
            print("\nItems in your cart:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Your cart is empty.")

def main():
    cart = ShoppingCart()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Display Items")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ")
            cart.add_item(item)
        elif choice == "2":
            item = input("Enter item to remove: ")
            cart.remove_item(item)
        elif choice == "3":
            cart.display_items()
        elif choice == "4":
            print("Thank you for using the shopping cart system!")
            break
        else:
            print("Invalid choice. Try again.")
main()
