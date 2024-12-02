class Library:
    total_books = 0

    def add(self, x):
        Library.total_books += x
        print("The total number of books",Library.total_books)

# Creating an object and adding books
obj1 = Library()
obj1.add(20)
obj1.add(20)

