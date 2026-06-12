class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def find_book(self, keyword):
        return [book for book in self.books.values()
                if keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword == book.isbn]

    def register_member(self, member):
        self.members[member.member_id] = member

    def find_member(self, member_id):
        return self.members.get(member_id, None)
