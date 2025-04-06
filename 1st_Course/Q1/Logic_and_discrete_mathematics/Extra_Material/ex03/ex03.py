class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search(current.left, key)
        return self._search(current.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, current, result):
        if current:
            self._inorder_traversal(current.left, result)
            result.append(current.key)
            self._inorder_traversal(current.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, current, result):
        if current:
            result.append(current.key)
            self._preorder_traversal(current.left, result)
            self._preorder_traversal(current.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, current, result):
        if current:
            self._postorder_traversal(current.left, result)
            self._postorder_traversal(current.right, result)
            result.append(current.key)


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]

    for el in elements:
        bst.insert(el)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Preorder Traversal:", bst.preorder_traversal())
    print("Postorder Traversal:", bst.postorder_traversal())

    search_key = 40
    found_node = bst.search(search_key)
    if found_node:
        print(f"Node with key {search_key} found.")
    else:
        print(f"Node with key {search_key} not found.")