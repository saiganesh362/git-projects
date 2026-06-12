import datetime

class Library(Library):  # extending previous Library
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.books.get(isbn)
        if member and book:
            return member.return_book(book)
        return False

    def statistics(self):
        total = len(self.books)
        available = sum(1 for b in self.books.values() if b.available)
        return {"total_books": total, "available_books": available}
