class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # stan książki

    def borrow(self) -> bool:
        """Zwraca True jeśli wypożyczenie się udało, False jeśli książka już jest wypożyczona."""
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_back(self) -> bool:
        """Zwraca True jeśli zwrot się udał, False jeśli książka nie była wypożyczona."""
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

    def __str__(self):
        status = "Wypożyczona" if self.is_borrowed else "Dostępna"
        return f"{self.title} ({self.year}) - {self.author} [{status}]"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"\nLibrary: {self.name}")
        print("Books:")
        for book in self.books:
            print(book)
