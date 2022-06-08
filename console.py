import pdb

from models.book import Book
from models.author import Author

import repositories.books_repository as book_repository
import repositories.author_repository as author_repository


author_repository.delete_all()

author_1 = Author("Plato")
author_repository.save(author_1)




pdb.set_trace()