class Address:
    def __init__(self, city, street, postal_code):
        self.city = city
        self.street = street
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}"


class Reader:
    def __init__(self, first_name, last_name, city, street, postal_code):
        self.first_name = first_name
        self.last_name = last_name

        # kompozycja
        self.address = Address(city, street, postal_code)

        # lista wypożyczonych książek (agregacja: trzymamy referencje do Book)
        self.borrowed_books = []

    def borrow_book(self, book) -> bool:
        """
        Próbuje wypożyczyć książkę.
        - jeśli book jest już wypożyczona: nie wypożyczy
        - jeśli dostępna: oznacza jako wypożyczoną i dodaje do listy czytelnika
        """
        if book.borrow():  # Book decyduje czy można
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book) -> bool:
        """
        Próbuje oddać książkę:
        - jeśli czytelnik jej nie ma: nie odda
        - jeśli ma: usuwa z listy i ustawia stan książki na dostępną
        """
        if book not in self.borrowed_books:
            return False

        if book.return_back():
            self.borrowed_books.remove(book)
            return True

        return False

    def list_borrowed_books(self):
        print(f"\nBorrowed books by {self.first_name} {self.last_name}:")
        if not self.borrowed_books:
            print("  (none)")
            return
        for b in self.borrowed_books:
            print(" ", b)

    def __str__(self):
        return f"Reader: {self.first_name} {self.last_name}\nAddress: {self.address}"
