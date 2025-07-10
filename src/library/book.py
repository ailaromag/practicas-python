import orjson

# Book class
class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    # Overriding the method that represents the object as a string
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available_copies}"

    # Saves a dictionary readable by the machine --> a structure
    # Transforms Book("El Principito", "Antoine", "123", 3) into a JSON structure
    def to_dict(self):
        return {
        "title": self.title,
        "author": self.author,
        "available_copies": self.available_copies
        }   
    

    # Loads a JSON, will be able to : book = Book.from_dict("123",data)
    @classmethod
    def from_dict(cls, isbn, data):
        return cls(
            title=data["title"],
            author=data["author"],
            isbn=isbn,
            available_copies=data["available_copies"]
        )