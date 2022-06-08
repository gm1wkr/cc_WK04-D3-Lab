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


def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING id"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author




def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM authors WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)