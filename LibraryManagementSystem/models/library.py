
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from models.reservable import Reservable
from exceptions.custom_exceptions import (
    ItemNotAvailableError, UserNotFoundError, ItemNotFoundError, ItemAlreadyReservedError
)

class Library:
    def __init__(self):
        self.items = []  # كل العناصر في المكتبة
        self.users = []  # كل المستخدمين
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item.title}' added to library.")
    
    def remove_item(self, item_title):
        try:
            item = self.find_item(item_title)
            self.items.remove(item)
            print(f"Item '{item_title}' removed.")
        except ItemNotFoundError as e:
            print(f"Error: {e}")
        finally:
            print("Remove item attempt complete.\n")
    
    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' added.")
    
    def remove_user(self, user_id):
        try:
            user = self.find_user(user_id)
            self.users.remove(user)
            print(f"User '{user.name}' removed.")
        except UserNotFoundError as e:
            print(f"Error: {e}")
        finally:
            print("Remove user attempt complete.\n")
    
    def borrow_item(self, user_id, item_title):
        try:
            user = self.find_user(user_id)
            item = self.find_item(item_title)
            
            if not item.check_availability():
                raise ItemNotAvailableError(f"Item '{item.title}' is not available for borrowing.")
            
            user.borrow_item(item)
            if hasattr(item, 'available'):
                item.available = False
            print(f"{user.name} borrowed '{item.title}'.")
        except (UserNotFoundError, ItemNotFoundError, ItemNotAvailableError) as e:
            print(f"Error: {e}")
        finally:
            print("Borrow attempt complete.\n")
    
    def return_item(self, user_id, item_title):
        try:
            user = self.find_user(user_id)
            found_item = None
            for item in user.borrowed_items:
                if item.title == item_title:
                    found_item = item
                    break
            
            if not found_item:
                raise ItemNotFoundError(f"Item '{item_title}' not found in user's borrowed items.")
            
            user.return_item(found_item)
            if hasattr(found_item, 'available'):
                found_item.available = True
            print(f"{user.name} returned '{found_item.title}'.")
        except (UserNotFoundError, ItemNotFoundError) as e:
            print(f"Error: {e}")
        finally:
            print("Return attempt complete.\n")
    
    def reserve_item(self, user_id, item_title):
        try:
            user = self.find_user(user_id)
            item = self.find_item(item_title)
            
            if not isinstance(item, Reservable):
                print(f"Item '{item.title}' cannot be reserved.")
                return
            
            if hasattr(item, 'reserved_by') and item.reserved_by is not None:
                raise ItemAlreadyReservedError(f"Item '{item.title}' is already reserved.")
            
            item.reserve(user.name)
        except (UserNotFoundError, ItemNotFoundError, ItemAlreadyReservedError) as e:
            print(f"Error: {e}")
        finally:
            print("Reserve attempt complete.\n")
    
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError(f"User with ID '{user_id}' not found.")
    
    def find_item(self, item_title):
        for item in self.items:
            if item.title == item_title:
                return item
        raise ItemNotFoundError(f"Item '{item_title}' not found.")
