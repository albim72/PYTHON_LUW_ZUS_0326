class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # lista książek

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"\nLibrary: {self.name}")
        print("Books:")

        for book in self.books:
            print(book)
