import logging
from library import Library

# Configure logging
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    library = Library()

    logging.info("Library application started")

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            if not book_id or not title or not author:
                print("Error: All fields are required.")
                logging.warning("Invalid input: Empty book details")
                continue

            try:
                message = library.add_book(book_id, title, author)
                print(message)
                logging.info("Book added: %s", title)

            except (ValueError, OSError) as error:
                print(f"Error: Unable to add book: {error}")
                logging.error("Failed to add book: %s", error)

        elif choice == "2":
            print(library.display_books())
            logging.info("Books displayed")

        elif choice == "3":
            print("Thank you for using the Library System!")
            logging.info("Library application closed")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            logging.warning("Invalid menu choice: %s", choice)


if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyboardInterrupt) as error:
        logging.error("Application interrupted or file error: %s", error)
        print("\nApplication stopped safely.")