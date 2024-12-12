class Library:
    def __init__(self):
        self.books = []  # Initializes an empty list to store books in the library

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def borrow_book(self, book):
        """Borrows a book from the library if available."""
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed the book '{book}'.")
        else:
            print(f"Sorry, the book '{book}' is not available in the library.")

    def display_books(self):
        """Displays all the books available in the library."""
        if self.books:
            print("\nBooks available in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books available in the library.")


# Main function to interact with the Library
def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Borrow Book")
        print("3. Display Books")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            book = input("Enter book title to add: ")
            library.add_book(book)
        elif choice == "2":
            book = input("Enter book title to borrow: ")
            library.borrow_book(book)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Try again.")


# Running the program
main()
