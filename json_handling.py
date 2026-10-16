import json

books = [
    {"name": "Python Basics", "author": "Guido"},
    {"name": "Learn SQL", "author": "John"},
    {"name": "HTML Basics", "author": "David"}
]

with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

print("Books saved to JSON successfully!")