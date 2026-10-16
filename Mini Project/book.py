class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_info(self):
        return f"{self.book_id}: {self.title} by {self.author}"