from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass
