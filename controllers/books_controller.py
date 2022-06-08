from flask import Flask, render_template, request, redirect
from models.book import Book
from repositories import books_repository, author_repository

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/tasks'
@books_blueprint.route("/books", methods=["GET"])
def books():
    books = books_repository.select_all()
    return render_template("books/index.html", all_books=books)

# New Book
# POST ''









# Show Single Book
# GET 'books/<id>'
@books_blueprint.route("/books/<id>", methods=["GET"])
def show_book(id):
    found_book = books_repository.select(id)
    return render_template("books/show.html", book=found_book)



# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    books_repository.delete(id)
    return redirect("/books")
