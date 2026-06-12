def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Show Statistics")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year: ")
            library.add_book(Book(title, author, isbn, year))
            print("Book added successfully!")

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            library.register_member(Member(name, member_id))
            print("Member registered successfully!")

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            if library.borrow_book(member_id, isbn):
                print("Book borrowed successfully!")
            else:
                print("Borrow failed.")

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            if library.return_book(member_id, isbn):
                print("Book returned successfully!")
            else:
                print("Return failed.")

        elif choice == "5":
            keyword = input("Search keyword: ")
            results = library.find_book(keyword)
            for book in results:
                print(book)

        elif choice == "6":
            stats = library.statistics()
            print(stats)

        elif choice == "7":
            break

if __name__ == "__main__":
    main()
