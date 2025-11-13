class Node:
    def __init__(self, key, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __contains__(self, key):
        return self.search(key) is not None

    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    current.left.parent = current
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key, value)
                    current.right.parent = current
                    return
                current = current.right
            else:
                current.value = value
                return

    def search(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current
        return None

    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError("Node with this key does not exist")
        self._delete(node)

    def _delete(self, node):
        # leaf node/ no child node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        # one child node
        elif node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if node.parent is None:
                self.root = child
                child.parent = None
            elif node.parent.left == node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
        # two child node
        else:
            successor = self._successor(node)
            node.key, node.value = successor.key, successor.value
            self._delete(successor)

    def _successor(self, node):
        current = node.right
        while current and current.left:
            current = current.left
        return current

    def _predecessor(self, node):
        current = node.left
        while current and current.right:
            current = current.right
        return current

    def traverse(self, order="inorder"):
        if order == "inorder":
            return self._in_order_traversal(self.root)
        elif order == "preorder":
            return self._pre_order_traversal(self.root)
        elif order == "postorder":
            return self._post_order_traversal(self.root)
        else:
            raise ValueError("Unknown traverse order")

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for key in [10, 5, 22, 2, 9, 12, 30, 11, 15, 30, 23, 35]:
        bst.insert(key, "Hello")

    print("Inorder Traversal (key, value):")
    for item in bst.traverse('inorder'):
        print(item)
