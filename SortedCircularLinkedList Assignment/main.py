from circular_linked_list import CircularLinkedList

scll = CircularLinkedList()

values = [7, 3, 9, 1, 4]

for value in values:
    print(f"Inserting {value}:")
    scll.insert(value)
    scll.print_list()
    print("-" * 30)
