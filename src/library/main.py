from book import Book
from library import Library

# Main function with menu
def menu():
    library = Library()
    while True:
        print("\nSelect an option:")
        print("1. Add book")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Borrow book")
        print("5. Return book")
        print("6. List all books")
        print("7. Exit")

        option = input("Option: ")

        if option == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            copies = int(input("Available copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book)
            print("Book added successfully.")

        elif option == "2":
            title = input("Search title: ")
            results = library.search_by_title(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found with that title.")

        elif option == "3":
            author = input("Search author: ")
            results = library.search_by_author(author)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found by that author.")

        elif option == "4":
            isbn = input("ISBN of the book to borrow: ")
            if library.borrow_book(isbn):
                print("Book successfully borrowed.")
            else:
                print("Book not available for borrowing.")

        elif option == "5":
            isbn = input("ISBN of the book to return: ")
            if library.return_book(isbn):
                print("Book successfully returned.")
            else:
                print("No book found with that ISBN.")

        elif option == "6":
            books = library.list_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("There are no books in the library.")

        elif option == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option.")


if __name__ == '__main__':
    menu()
