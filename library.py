import csv
import logging
from book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Library:
    def __init__(self):
        self.books = []
        self.file_name = "books.csv"
        self.load_books()

    def add_book(self, book_id, title, author):
        book_id = book_id.strip()
        title = title.strip()
        author = author.strip()

        if not book_id or not title or not author:
            return "Error: All fields are required."

        for book in self.books:
            if book.book_id == book_id:
                logging.warning("Duplicate book ID: %s", book_id)
                return f"Error: Book ID '{book_id}' already exists."

        book = Book(book_id, title, author)
        self.books.append(book)

        try:
            self.save_books()
        except (OSError, csv.Error) as error:
            self.books.pop()
            logging.error("Failed to save book: %s", error)
            return f"Error: Unable to save book: {error}"

        logging.info("Book added: %s", title)
        return f"Book '{title}' added successfully."

    def display_books(self):
        if not self.books:
            return "No books available."

        return "\n".join(
            book.display_info() for book in self.books
        )

    def save_books(self):
        with open(
            self.file_name,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author"])

            for book in self.books:
                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author
                ])

    def load_books(self):
        try:
            with open(
                self.file_name,
                "r",
                newline="",
                encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)

                required_fields = {"book_id", "title", "author"}

                if not required_fields.issubset(
                    reader.fieldnames or []
                ):
                    raise ValueError("Invalid CSV header.")

                loaded_books = []
                seen_ids = set()

                for row in reader:
                    book_id = (row.get("book_id") or "").strip()
                    title = (row.get("title") or "").strip()
                    author = (row.get("author") or "").strip()

                    if not book_id or not title or not author:
                        logging.warning(
                            "Skipped CSV row with missing fields."
                        )
                        continue

                    if book_id in seen_ids:
                        logging.warning(
                            "Skipped duplicate book ID: %s", book_id
                        )
                        continue

                    loaded_books.append(Book(book_id, title, author))
                    seen_ids.add(book_id)

                self.books = loaded_books

        except FileNotFoundError:
            logging.info("Books CSV not found; starting with empty library.")

        except (OSError, csv.Error, ValueError) as error:
            logging.error("Unable to load books: %s", error)
def test_duplicate_book_id(tmp_path):
    library = Library()
    library.books = []
    library.file_name = str(tmp_path / "books.csv")

    library.add_book(
        "101", "Python Basics", "Guido van Rossum"
    )

    message = library.add_book(
        "101", "Python Advanced", "Divya"
    )

    assert message == "Error: Book ID '101' already exists."
    assert len(library.books) == 1