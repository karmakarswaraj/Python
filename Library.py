#Write a Library class with no_of_books and books as two instance variables. 
#Write a program to create a library from this Library class and show how you can print all books,
    # add a book and get the number of books using different methods.
#Show that your program doesnt persist the books after the program is stopped!

class Lib:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addbooks(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The library has {self.no_of_books} books. The books are")
        for book in self.books:
            print(book)


l1 = Lib()
l1.addbooks("Harry Potter1")
l1.addbooks("Harry Potter2")
l1.addbooks("Harry Potter3")
l1.showInfo()

