import os
import orjson

class Library:
    def __init__(self):
        self.books = {}  # Dictionary: key = ISBN, value = Book object

    # Methods:
    def add_book(self, book):
        # First, check if the book already exists by ISBN
        if book.isbn in self.books:
            self.books[book.isbn].available_copies += book.available_copies
        else:
            self.books[book.isbn] = book

    def search_by_title(self, title:str):
        results = []
        for book in self.books.values():
            if book.title.lower() == title.lower():
                results.append(book)       
        return results
    
    def search_by_author(self,author:str):
        results = []
        for book in self.books.values():
            if book.author.lower() == author.lower():
                results.append(book)
        return results
    
    def borrow_book(self,isbn:str):
        if isbn in self.books:
            if self.books[isbn].available_copies > 0:
                self.books[isbn].available_copies -= 1
                return True
        return False
        


    def return_book(self,isbn:str):
        if isbn in self.books:
            self.books[isbn].available_copies +=1
            return True
        return False
    

    def list_books(self):
        return list(self.books.values())
    

    # TODO: implement JSON--> check how it works

    
    def save(self,filename:str):
    # 1. Convert all books to dictionary
        data = {isbn: book.to_dict() for isbn, book in self.books.items()}
        os.makedirs("data",exist_ok=True) # We create the /data directory
        with open(f"data/{filename}","wb") as f:
           f.write(orjson.dumps(data))
        print(data)


    def load(self, filename: str):
        try:
            with open(f"data/{filename}", "rb") as f:
                data = orjson.loads(f.read())
                self.books = {
                    isbn: Book.from_dict(isbn, book_data)
                    for isbn, book_data in data.items()
                }
            print(f"Library loaded from data/{filename}")
        except FileNotFoundError:
            print("File not found.")
