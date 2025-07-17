from collections import deque

# Create an empty queue
queue = deque()

# Enqueue customer names
customers = ["Alaa", "Hadeel", "Karema","manar"]
for customer in customers:
    print(f"Arriving: {customer}")
    queue.append(customer)

# Dequeue and serve customers
while queue:
    served_customer = queue.popleft()
    print(f"Serving: {served_customer}")

# When queue is empty
print("All customers served.")
