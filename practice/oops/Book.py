class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def display_book_description(self):
        print("Book title : ", self.title, " and author : ",
              self.author, "inside method and genre is : ", self.get_genre())


book = Book("Kota Factory", "jeetu bhaiya", "inspirational")
print("Book title : ", book.title, " and author : ", book.author)
book.display_book_description()
