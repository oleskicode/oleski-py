class Book:
    book_name = ""
    pages = 0

    def __init__(self, book_name, pages):
        self.book_name = book_name
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.book_name} is {self.pages} pages long"

    def __repr__(self):
        representation = (f"type(self): {str(type(self))} \n"
                          f"self.book_name: {self.book_name} \n"
                          f"self.pages : {self.pages}")
        return representation

book1 = Book("Fairy tales", 100)
print(book1.__str__())
print(book1.__repr__())
