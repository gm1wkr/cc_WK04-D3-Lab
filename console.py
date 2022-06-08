import pdb

from models.book import Book
from models.author import Author

import repositories.books_repository as book_repository
import repositories.author_repository as author_repository


book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Plato")
author_repository.save(author_1)

author_2 = Author("Grant Nailor")
author_repository.save(author_2)

author_3 = Author("Arthur C Clarke")
author_repository.save(author_3)


author_list = author_repository.select_all()
# author_repository.delete(author_list[2].id)
# author_list = author_repository.select_all()

book_1 = Book("the Republic", author_1, "Classics")
book_repository.save(book_1)

book_2 = Book("Red Dwarf", author_2, "Science Fiction")
book_repository.save(book_2)

book_3 = Book("Blardy Blah", author_1, "Classics")
book_repository.save(book_3)

book_4 = Book("Dolphin Island", author_3, "Adventure")
book_repository.save(book_4)

book_5 = Book("Children of tomorrow", author_1, "Science Fiction")
book_repository.save(book_5)

book_6 = Book("Rendevous with Rama", author_3, "Science Fiction")
book_repository.save(book_6)

books = book_repository.select_all()

pdb.set_trace()