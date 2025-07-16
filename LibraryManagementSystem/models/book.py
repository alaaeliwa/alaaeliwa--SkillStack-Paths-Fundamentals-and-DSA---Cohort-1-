from models.library_item import LibraryItem
from models.reservable import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn
        self.available = True
        self.reserved_by = None

    def display_info(self):
        print(f"Book: {self.title} by {self.author}, ISBN: {self.isbn}")

    def check_availability(self):
        return self.available

    def reserve(self, user):
        if self.available and self.reserved_by is None:
            self.reserved_by = user.name  # أو user مباشرة حسب الاستخدام
            print(f"{user.name} reserved the book '{self.title}'.")
        else:
            raise Exception(f"Sorry, the book '{self.title}' is not available for reservation.")
