class Book:
    def __init__(self, title, author, isbn):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string.")
        if not isbn or not isinstance(isbn, str):
            raise ValueError("ISBN must be a non-empty string.")

        self.__title = title
        self.__author = author
        self.__isbn = isbn

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    # Display method
    def display_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}"


class Library:
    def __init__(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Library name must be a non-empty string.")

        self.__name = name
        self.__books = []  # Composition happens here
        print( "Library created")

    # Add a book
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added.")

        # Prevent duplicate ISBN
        for existing_book in self.__books:
            if existing_book.get_isbn() == book.get_isbn():
                print("Book with this ISBN already exists.")
                return

        self.__books.append(book)
        print(f"Book '{book.get_title()}' added successfully.")

    # Remove book by ISBN
    def remove_book(self, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn:
                self.__books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    # List all books
    def list_books(self):
        if not self.__books:
            print("No books in library.")
            return

        for book in self.__books:
            print(book.display_info())

    # Search by title (case insensitive)
    def search_by_title(self, title):
        results = []
        for book in self.__books:
            if title.lower() in book.get_title().lower():
                results.append(book)

        if not results:
            print("No matching books found.")
        else:
            print("Search Results:")
            for book in results:
                print(book.display_info())



# testing checklist
# Create books
book1 = Book("1984", "George Orwell", "123456")
book2 = Book("Brave New World", "Aldous Huxley", "789101")
book3 = Book("Python Programming", "John Smith", "112233")

# Create library
my_library = Library("City Library")

# Add books
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# List books
my_library.list_books()

# Search book
my_library.search_by_title("python")

# Remove book
my_library.remove_book("789101")

# List again
my_library.list_books()