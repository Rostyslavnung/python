from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple, Any

@dataclass
class Book:
    """Represents a single book."""
    author: str
    title: str
    publisher: str
    genre: str
    year: int

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class HomeLibrary:
    """
    HomeLibrary holds Book instances indexed by integer IDs.
    Search supports:
      - substring match for string fields (case-insensitive),
      - exact match for non-strings,
      - range for numeric fields if you pass a 2-tuple (min, max),
      - membership if you pass a list/tuple/set of allowed values.
    """
    def __init__(self) -> None:
        self._books: Dict[int, Book] = {}
        self._next_id: int = 1

    def add_book(self, book: Book, book_id: Optional[int] = None) -> int:
        """Add a book. If book_id is None, it is auto-assigned. Returns the id used."""
        if book_id is None:
            book_id = self._next_id
            self._next_id += 1
        else:
            if book_id in self._books:
                raise ValueError(f"Book id {book_id} already exists.")
            if book_id >= self._next_id:
                self._next_id = book_id + 1
        self._books[book_id] = book
        return book_id

    def remove_book(self, book_id: int) -> Optional[Book]:
        """Remove and return the book by id, or None if not found."""
        return self._books.pop(book_id, None)

    def get_book(self, book_id: int) -> Optional[Book]:
        """Return Book or None if not found."""
        return self._books.get(book_id)

    def update_book(self, book_id: int, **fields) -> bool:
        """
        Update fields of a book (author, title, publisher, genre, year).
        Returns True if updated, False if book_id not found.
        """
        book = self._books.get(book_id)
        if not book:
            return False
        for k, v in fields.items():
            if hasattr(book, k):
                setattr(book, k, v)
        return True

    def search_books(self, **criteria) -> List[Tuple[int, Book]]:
        """
        Search books by named criteria.
        Examples:
          search_books(author="Tolkien")            # substring match (case-insensitive)
          search_books(year=(1930,1950))           # year in range inclusive
          search_books(genre=["Fantasy","Sci-Fi"]) # genre in list
          search_books(year=1997)                  # exact numeric match
        Returns list of (id, Book).
        """
        results: List[Tuple[int, Book]] = []
        for bid, book in self._books.items():
            ok = True
            for key, value in criteria.items():
                attr = getattr(book, key, None)
                if attr is None:
                    ok = False
                    break
                if isinstance(value, (list, tuple)) and len(value) == 2 and \
                   all(isinstance(x, (int, float)) for x in value):
                    if not (value[0] <= attr <= value[1]):
                        ok = False
                        break
                elif isinstance(value, (list, tuple, set)):
                    if attr not in value:
                        ok = False
                        break
                elif isinstance(value, str) and isinstance(attr, str):
                    if value.lower() not in attr.lower():
                        ok = False
                        break
                else:
                    if attr != value:
                        ok = False
                        break
            if ok:
                results.append((bid, book))
        return results

    def list_books(self) -> List[Tuple[int, Book]]:
        """Return list of (id, Book)."""
        return list(self._books.items())

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books.items())


if __name__ == "__main__":
    lib = HomeLibrary()
    b1 = Book("J.R.R. Tolkien", "The Hobbit", "Allen & Unwin", "Fantasy", 1937)
    b2 = Book("George Orwell", "1984", "Secker & Warburg", "Dystopian", 1949)
    id1 = lib.add_book(b1)
    id2 = lib.add_book(b2)

    print("All books:", [(i, str(b)) for i,b in lib.list_books()])

    print("Search author 'Tolkien':", lib.search_books(author="Tolkien"))

    print("Books 1930-1940:", lib.search_books(year=(1930,1940)))

    lib.update_book(id2, publisher="Penguin Classics")
    print("Updated:", lib.get_book(id2).to_dict())
