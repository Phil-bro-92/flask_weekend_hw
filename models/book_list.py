from models.book import Book


book_1 = Book("Game of Thrones", "George R R Martin", "Fantasy", True)
book_2 = Book("The Bourne Identity", "Robert Ludlum", "Action/Thriller", False)
book_3 = Book("The Catcher in the Rye", "J.D Salinger", "Coming of Age", False )
book_4 = Book("To Kill a Mockingbird", "Harper Lee", "Southern Gothic", True)
book_5 = Book("Harry Potter", "J.K Rowling", "Fantasy/Children", True)
books = [book_1, book_2, book_3, book_4, book_5]


def add_new_book(book):
    books.append(book)


def remove_book(book_index):
    del books[book_index]
