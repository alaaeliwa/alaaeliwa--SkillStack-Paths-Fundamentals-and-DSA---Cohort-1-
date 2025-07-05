from node import Node 

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head

        if value < self.head.data:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        while current.next != self.head and current.next.data < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while True:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()
