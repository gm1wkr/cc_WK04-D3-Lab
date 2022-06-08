from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.books_repository as books_repository

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = Book()
        books.append(books)

    return books


def save(book):
    sql = "INSERT INTO books (title, author_id, genre) VALUES (%s, %s, %s) RETURNING id"
    values = [book.title, book.author.id, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def update(book):
    sql = "UPDATE tasks SET (d) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.user.id, book.genre]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)