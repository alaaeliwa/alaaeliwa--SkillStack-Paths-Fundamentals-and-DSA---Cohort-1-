from models.library_item import LibraryItem
from models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration
        self.available = True
        self.reserved_by = None

    def display_info(self):
        print(f"DVD: {self.title} by {self.author}, Duration: {self.duration} mins")

    def check_availability(self):
        return self.available

    def reserve(self, user):
        if self.available and self.reserved_by is None:
            self.reserved_by = user.name
            print(f"{user.name} reserved the DVD '{self.title}'.")
        else:
            raise Exception(f"Sorry, the DVD '{self.title}' is not available for reservation.")
