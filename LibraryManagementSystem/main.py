import json
from models.library import Library
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from exceptions.custom_exceptions import ItemNotFoundError, UserNotFoundError

ITEMS_FILE = 'data/items.json'
USERS_FILE = 'data/users.json'


def load_items():
    items = []
    try:
        with open(ITEMS_FILE, 'r') as f:
            data = json.load(f)
            for item_data in data:
                # بناء العنصر حسب النوع
                if item_data['type'] == 'Book':
                    item = Book(item_data['title'], item_data['author'], item_data.get('isbn',''))
                    item.available = item_data.get('available', True)
                    item.reserved_by = item_data.get('reserved_by', None)
                    items.append(item)
                elif item_data['type'] == 'Magazine':
                    item = Magazine(item_data['title'], item_data['author'], item_data.get('issue',''))
                    item.available = item_data.get('available', True)
                    items.append(item)
                elif item_data['type'] == 'DVD':
                    item = DVD(item_data['title'], item_data['author'], item_data.get('duration',''))
                    item.available = item_data.get('available', True)
                    item.reserved_by = item_data.get('reserved_by', None)
                    items.append(item)
    except FileNotFoundError:
        print(f"{ITEMS_FILE} not found, starting with empty items list.")
    except json.JSONDecodeError:
        print(f"Error decoding {ITEMS_FILE}, starting with empty items list.")
    return items

def load_users():
    users = []
    try:
        with open(USERS_FILE, 'r') as f:
            data = json.load(f)
            for user_data in data:
                user = User(user_data['user_id'], user_data['name'])
                # استرجاع العناصر المستعارة يمكن تنفيذها لاحقًا حسب تصميمك
                users.append(user)
    except FileNotFoundError:
        print(f"{USERS_FILE} not found, starting with empty users list.")
    except json.JSONDecodeError:
        print(f"Error decoding {USERS_FILE}, starting with empty users list.")
    return users

def save_items(items):
    try:
        data = []
        for item in items:
            item_dict = {
                'title': item.title,
                'author': item.author,
                'available': getattr(item, 'available', True),
                'reserved_by': getattr(item, 'reserved_by', None),
            }
            # نضيف نوع العنصر وخصائص محددة لكل نوع
            if isinstance(item, Book):
                item_dict['type'] = 'Book'
                item_dict['isbn'] = getattr(item, 'isbn', '')
            elif isinstance(item, Magazine):
                item_dict['type'] = 'Magazine'
                item_dict['issue'] = getattr(item, 'issue', '')
            elif isinstance(item, DVD):
                item_dict['type'] = 'DVD'
                item_dict['duration'] = getattr(item, 'duration', '')
            data.append(item_dict)
        with open(ITEMS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving items: {e}")

def save_users(users):
    try:
        data = []
        for user in users:
            user_dict = {
                'user_id': user.user_id,
                'name': user.name,
                # يمكن إضافة borrowed_items إذا أردت حفظها في الملف
            }
            data.append(user_dict)
        with open(USERS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving users: {e}")

def main_menu():
    print("""
Welcome to the Library System
1. View all available items
2. Search item by title or type
3. Register as a new user
4. Borrow an item
5. Reserve an item
6. Return an item
7. Exit and Save
""")

def main():
    library = Library()
    library.items = load_items()
    library.users = load_users()

    while True:
        main_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            print("Available items:")
            for item in library.items:
                status = "Available" if getattr(item, 'available', True) else "Not Available"
                print(f"- [{item.__class__.__name__}] Title: {item.title} | Author: {item.author} | Status: {status}")
        
        elif choice == '2':
            keyword = input("Enter search keyword (title or type): ").strip().lower()
            results = []
            for item in library.items:
                if (keyword in item.title.lower()) or (keyword == item.__class__.__name__.lower()):
                    results.append(item)
            if results:
                print("Search Results:")
                for item in results:
                    status = "Available" if getattr(item, 'available', True) else "Not Available"
                    print(f"- [{item.__class__.__name__}] Title: {item.title} | Author: {item.author} | Status: {status}")
            else:
                print("No matching items found.")
        
        elif choice == '3':
            name = input("Enter your name: ").strip()
            # بسيط، user_id زي عدد المستخدمين + 1
            user_id = max([u.user_id for u in library.users], default=0) + 1
            new_user = User(user_id, name)
            library.add_user(new_user)
            print(f"User registered with ID: {user_id}")
        
        elif choice == '4':
            try:
                user_id = int(input("Enter your user ID: ").strip())
                item_title = input("Enter item title to borrow: ").strip()
                library.borrow_item(user_id, item_title)
            except ValueError:
                print("Invalid input for user ID.")
        
        elif choice == '5':
            try:
                user_id = int(input("Enter your user ID: ").strip())
                item_title = input("Enter item title to reserve: ").strip()
                library.reserve_item(user_id, item_title)
            except ValueError:
                print("Invalid input for user ID.")
        
        elif choice == '6':
            try:
                user_id = int(input("Enter your user ID: ").strip())
                item_title = input("Enter item title to return: ").strip()
                library.return_item(user_id, item_title)
            except ValueError:
                print("Invalid input for user ID.")
        
        elif choice == '7':
            print("Saving data and exiting...")
            save_items(library.items)
            save_users(library.users)
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
