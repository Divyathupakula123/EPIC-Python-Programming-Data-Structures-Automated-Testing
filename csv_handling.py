import csv

books = [
    ["Book Name", "Author"],
    ["Python Basics", "Guido"],
    ["Learn SQL", "John"],
    ["HTML Basics", "David"]
]

with open("books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books)

print("Books saved successfully!")