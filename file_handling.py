book_name = input("Enter book name: ")

with open("book.txt", "w") as file:
    file.write(book_name)

print("Book name saved successfully!")