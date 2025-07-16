
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []  # قائمة العناصر المستعارة
    
    def borrow_item(self, item):
        self.borrowed_items.append(item)
    
    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
        else:
            print(f"Item '{item.title}' not found in {self.name}'s borrowed items.")
    
    def display_borrowed_items(self):
        if not self.borrowed_items:
            print(f"{self.name} has no borrowed items.")
        else:
            print(f"{self.name} borrowed:")
            for item in self.borrowed_items:
                item.display_info()
