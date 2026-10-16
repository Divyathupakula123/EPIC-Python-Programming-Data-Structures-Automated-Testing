class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


book1 = Book("Python Basics", "Ravi")

book1.display_details()