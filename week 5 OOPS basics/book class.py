class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"

    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True
