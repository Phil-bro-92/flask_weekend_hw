from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, remove_book
from models.book import Book


@app.route("/books")
def get_books():
    return render_template("index.html", title="Home", books=books)


@app.route("/books/<int:id>")
def get_a_book(id):
    return render_template("book.html", title="Home", book=books[id])


@app.route("/books", methods=["POST"])
def add_book():
    book_title = request.form["book-title"]
    book_author = request.form["book-author"]
    book_genre = request.form["book-genre"]
    checked_out = True if 'checked-out' in request.form else False
    new_book = Book(book_title, book_author, book_genre, checked_out)
    add_new_book(new_book)
    return render_template("index.html", title="Home", books=books)


@app.route("/books/delete/<int:id>", methods=["POST"])
def delete_book(id):
    remove_book(id)
    return redirect('/books')
