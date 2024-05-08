from author import Author

class Books():
    def __init__(self, title, author, isbn, genre, pub_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.pub_date = pub_date
        self.is_available = True

    def get_info(self):
        return f"{self.title} {self.author} {self.isbn} {self.genre} {self.pub_date} {self.is_available}"
    