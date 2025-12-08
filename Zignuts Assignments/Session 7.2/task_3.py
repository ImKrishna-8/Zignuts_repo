class library:
    book_title="default name"
    book_price = 0

    def __init__(self,book_title,book_price):
        self.book_title = book_title
        self.book_price = book_price

books = [] 

def add_book():
    name = input("Enter book1 name: ")
    price = input("Enter book1 Price: ")
    return library(name,price)

def remove_book(name):
    for book in books:
        if(book.book_title == name):
            print("book deleted successfully")
            books.remove(book)
            return
    print("No book found ! ")

def show_all():
    print("TOTAL BOOKS : ",len(books))
    for book in books:
        print("------------------------")
        print("name: ",book.book_title)
        print("price: ",book.book_price)
        print("------------------------")

def search_book():
    find= input("Enter book name you want to search:")
    for book in books:
        if(book.book_title == find):
            print("Yes Book available")
            return
    print("Not any book with that name")
    
    
books.append(add_book())
books.append(add_book())
books.append(add_book())
books.append(add_book())

name = input("Enter Book name you want to delete: ")
remove_book(name)

search_book();
show_all();