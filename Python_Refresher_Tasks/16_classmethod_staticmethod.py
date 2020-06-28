class classTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def classmethod(cls):
        print(f"Called class_method")

    @staticmethod
    def static_method():
        print("Callled static_method")


#Example

class Book:
    TYPES = ("hardcover","paperback")

    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weihging {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0],page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1],page_weight+100)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(f"Book: {book}, Light : {light}")
    