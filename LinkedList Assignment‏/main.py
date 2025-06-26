from linked_list import LinkedList
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)

print("Before reversing:")
print(ll)

ll.reverse()

print("After reversing:")
print(ll)
