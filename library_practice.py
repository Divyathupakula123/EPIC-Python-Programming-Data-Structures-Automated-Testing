book_name = input("Enter book name: ").strip()
author_name = input("Enter author name: ").strip()

if not book_name or not author_name:
    print("Error: Book name and author name cannot be empty.")

else:
    print("Book added successfully!")
    print("Book name:", book_name)
    print("Author name:", author_name)