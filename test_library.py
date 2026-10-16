from book import Book
from library import Library


def test_book_display_info():
    book = Book("101", "Python Basics", "Guido van Rossum")

    assert book.display_info() == (
        "101: Python Basics by Guido van Rossum"
    )


def test_add_book(tmp_path):
    library = Library()
    library.books = []
    library.file_name = str(tmp_path / "books.csv")

    message = library.add_book(
        "101", "Python Basics", "Guido van Rossum"
    )

    assert message == "Book 'Python Basics' added successfully."
    assert len(library.books) == 1


def test_display_books(tmp_path):
    library = Library()
    library.books = []
    library.file_name = str(tmp_path / "books.csv")

    library.add_book(
        "101", "Python Basics", "Guido van Rossum"
    )

    result = library.display_books()

    assert "Python Basics" in result
    assert "Guido van Rossum" in result


def test_empty_library(tmp_path):
    library = Library()
    library.books = []
    library.file_name = str(tmp_path / "empty_books.csv")

    assert library.display_books() == "No books available."
def test_duplicate_book_id(tmp_path):
    library = Library()
    library.books = []
    library.file_name = str(tmp_path / "duplicate_books.csv")

    library.add_book(
        "101", "Python Basics", "Guido van Rossum"
    )

    message = library.add_book(
        "101", "Python Advanced", "Divya"
    )

    assert message == "Error: Book ID '101' already exists."
    assert len(library.books) == 1