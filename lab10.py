from dotenv import load_dotenv
import psycopg2
import os
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
    def __init__(self) -> None:
        self._books: Dict[int, Book] = {}
        self._next_id: int = 1

    def init_db(self, conn):
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    author TEXT NOT NULL,
                    title TEXT NOT NULL,
                    publisher TEXT,
                    genre TEXT,
                    year INT
                );
            """)
        conn.commit()

    def delete_from_db(self, conn, book_id: int) -> bool:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM books WHERE id = %s RETURNING id;", (book_id,))
            deleted = cur.fetchone()
        conn.commit()
        return deleted is not None

    def save_to_db(self, conn, book: Book) -> int:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO books (author, title, publisher, genre, year)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """, (book.author, book.title, book.publisher, book.genre, book.year))
            book_id = cur.fetchone()[0]
        conn.commit()
        return book_id

    def search_in_db(self, conn, **criteria):
        query = "SELECT id, author, title, publisher, genre, year FROM books WHERE TRUE"
        values = []

        for key, value in criteria.items():
            if key in ["author", "title", "publisher", "genre"]:
                query += f" AND {key} ILIKE %s"
                values.append(f"%{value}%")
            elif key == "year":
                if isinstance(value, tuple) and len(value) == 2:
                    query += " AND year BETWEEN %s AND %s"
                    values.extend(value)
                else:
                    query += " AND year = %s"
                    values.append(value)

        with conn.cursor() as cur:
            cur.execute(query, values)
            rows = cur.fetchall()

        return [(r[0], Book(r[1], r[2], r[3], r[4], r[5])) for r in rows]

    def drop_table(self, conn):
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS books;")
        conn.commit()

if __name__ == "__main__":
    load_dotenv()
    conn_str = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(conn_str)

    lib = HomeLibrary()
    lib.init_db(conn)

    b1 = Book("J.R.R. Tolkien", "The Hobbit", "Allen & Unwin", "Fantasy", 1937)
    b2 = Book("George Orwell", "1984", "Secker & Warburg", "Dystopian", 1949)

    id1 = lib.save_to_db(conn, b1)
    id2 = lib.save_to_db(conn, b2)

    print("From DB:", lib.search_in_db(conn, author="Tolkien"))
    print("Books 1930–1940:", lib.search_in_db(conn, year=(1930,1940)))

    lib.delete_from_db(conn, id2)
    print("After delete:", lib.search_in_db(conn))

    #lib.drop_table(conn) 
