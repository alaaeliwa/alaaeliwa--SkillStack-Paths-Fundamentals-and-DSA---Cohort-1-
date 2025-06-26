from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += f"[{temp.data}]->"
            temp = temp.next
        result += "None"
        return result

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # حفظ المؤشر التالي
            current.next = prev       # عكس الاتجاه
            prev = current            # تحديث السابق
            current = next_node       # الانتقال للعنصر التالي
        self.head = prev  # تحديث رأس القائمة