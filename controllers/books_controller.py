from click import edit
from flask import Flask, render_template, request, redirect
from models.book import Book
from repositories import books_repository, author_repository

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books", methods=["GET"])
def books():
    books = books_repository.select_all()
    return render_template("books/index.html", all_books=books)

# New Book
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)


# Create 
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    books_repository.save(book)
    return redirect("/books")



# Show Single Book
# GET 'books/<id>'
@books_blueprint.route("/books/<id>", methods=["GET"])
def show_book(id):
    found_book = books_repository.select(id)
    return render_template("books/show.html", book=found_book)


# EDIT
# GET '/books/<id>'
@books_blueprint.route("/books/<id>/edit", methods=["GET"])
def edit_book(id):
    book = books_repository.select(id)
    authors = author_repository.select_all()
    return render_template("/books/edit.html", book=book, all_authors=authors)



# UPDATE
# PUT (POST) '/books/<id>'
@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = Book(title, author, genre, id)
    books_repository.update(book)
    return redirect("/books")





# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    books_repository.delete(id)
    return redirect("/books")
