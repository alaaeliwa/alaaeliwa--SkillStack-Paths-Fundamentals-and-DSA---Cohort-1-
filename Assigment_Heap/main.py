class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a value and maintain heap property."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the max element from the heap."""
        if not self.heap:
            raise IndexError("Pop from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)
        return root_value

    def _heapify_up(self, index):
        """Move the element at index up to maintain heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Move the element at index down to maintain heap property."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break


if __name__ == "__main__":
    numbers = [15, 3, 17, 10, 84, 19, 6, 22, 9]
    heap = MaxHeap()

    print("Inserting numbers:", numbers)
    for num in numbers:
        heap.insert(num)
        print("Heap:", heap.heap)

    print("\nPopping elements in descending order:")
    while heap.heap:
        print(heap.pop(), end=" ")
