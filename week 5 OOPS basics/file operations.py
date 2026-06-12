import json

class Library(Library):
    def save_books(self, filename="books.json"):
        with open(filename, "w") as f:
            json.dump([vars(b) for b in self.books.values()], f)

    def load_books(self, filename="books.json"):
        try:
            with open(filename, "r") as f:
                books_data = json.load(f)
                for b in books_data:
                    book = Book(b['title'], b['author'], b['isbn'], b['year'])
                    book.available = b['available']
                    self.add_book(book)
        except FileNotFoundError:
            print("Books file not found.")

    def save_members(self, filename="members.json"):
        with open(filename, "w") as f:
            json.dump([{"name": m.name, "member_id": m.member_id} for m in self.members.values()], f)

    def load_members(self, filename="members.json"):
        try:
            with open(filename, "r") as f:
                members_data = json.load(f)
                for m in members_data:
                    member = Member(m['name'], m['member_id'])
                    self.register_member(member)
        except FileNotFoundError:
            print("Members file not found.")
