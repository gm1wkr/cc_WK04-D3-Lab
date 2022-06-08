import pdb

from models.book import Book
from models.author import Author

import repositories.books_repository as book_repository
import repositories.author_repository as author_repository


book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Plato")
author_repository.save(author_1)

author_2 = Author("Socrates")
author_repository.save(author_2)


author_list = author_repository.select_all()
# author_repository.delete(author_list[2].id)
# author_list = author_repository.select_all()

book_1 = Book("the Republic", author_1, "Classics")
book_repository.save(book_1)

book_2 = Book("the Apology", author_2, "Classics")
book_repository.save(book_2)

book_3 = Book("Blardy Blah", author_1, "Classics")
book_repository.save(book_3)

books = book_repository.select_all()

pdb.set_trace()