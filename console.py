import pdb

from models.book import Book
from models.author import Author

import repositories.books_repository as book_repository
import repositories.author_repository as author_repository


author_repository.delete_all()

author_1 = Author("Plato")
author_repository.save(author_1)

author_2 = Author("Socrates")
author_repository.save(author_2)

author_3 = Author("Lilly Savage")
author_repository.save(author_3)

author_list = author_repository.select_all()
author_repository.delete(author_list[2].id)

author_list = author_repository.select_all()

pdb.set_trace()