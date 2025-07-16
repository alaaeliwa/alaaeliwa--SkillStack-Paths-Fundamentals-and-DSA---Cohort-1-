
from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def display_info(self):
        print(f"Magazine: {self.title} by {self.author}, Issue: {self.issue_number}")
    
    def check_availability(self):
        # لنفترض المجلات دائما متوفرة للقراءة في المكتبة
        return True
