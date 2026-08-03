# Library Management System using OOP

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
        print()


class Patron:

    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print("Patron ID:", self.patron_id)
        print("Name:", self.name)

        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(book)

        print()


class Library:

    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print("Patron registered successfully.")

    def borrow_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print("Book borrowed successfully.")

    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print("Book returned successfully.")
        else:
            print("This patron did not borrow this book.")

    def display_books(self):

        if len(self.books) == 0:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display()

    def display_patrons(self):

        if len(self.patrons) == 0:
            print("No patrons registered.")
        else:
            for patron in self.patrons.values():
                patron.display()


# ------------------- Main Program -------------------

library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":

        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_book(patron_id, book_id)

    elif choice == "4":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_book(patron_id, book_id)

    elif choice == "5":

        library.display_books()

    elif choice == "6":

        library.display_patrons()

    elif choice == "7":

        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")