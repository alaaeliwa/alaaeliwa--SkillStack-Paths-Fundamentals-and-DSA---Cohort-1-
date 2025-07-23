class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert value into BST
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Find Minimum Value
    def findMin(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    # Find Maximum Value
    def findMax(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

# check if a binary tree is balanced
def isBalanced(root):
    def check(node):
        if not node:
            return 0, True

        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        balanced = (left_balanced and right_balanced and
                    abs(left_height - right_height) <= 1)
        height = 1 + max(left_height, right_height)

        return height, balanced

    _, result = check(root)
    return result


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(3)
bst.insert(7)
bst.insert(97)
bst.insert(98)

print("Min:", bst.findMin())  # Output: 3
print("Max:", bst.findMax())  # Output: 98
print("Is Balanced:", isBalanced(bst.root)) #false

