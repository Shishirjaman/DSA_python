class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return '[' + ', '.join(values) + ']'

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        current = self.head
        for _ in range(index - 1):
            if not current or not current.next and _ != index - 2:
                raise ValueError("Index out of bounds")
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        new_node.previous = current
        if current.next:
            current.next.previous = new_node
        else:
            self.tail = new_node
        current.next = new_node

    def delete(self, value):
        current = self.head
        if not current:
            raise ValueError("Empty linked list")
        # Delete head
        if current.value == value:
            self.head = current.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            return
        while current and current.value != value:
            current = current.next
        if not current:
            raise ValueError("Value not found")
        if current.next:
            current.next.previous = current.previous
        else:
            self.tail = current.previous
        if current.previous:
            current.previous.next = current.next

    def pop(self, index):
        if not self.head:
            raise ValueError("Index out of bounds")
        if index == 0:
            to_delete = self.head
            self.head = to_delete.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            return
        current = self.head
        for _ in range(index):
            if not current:
                raise ValueError("Index out of bounds")
            current = current.next
        if not current:
            raise ValueError("Index out of bounds")
        if current.next:
            current.next.previous = current.previous
        else:
            self.tail = current.previous
        if current.previous:
            current.previous.next = current.next

    def get(self, index):
        if not self.head:
            raise ValueError("Index out of bounds")
        current = self.head
        for _ in range(index):
            if not current.next:
                raise ValueError("Index out of bounds")
            current = current.next
        return current.value

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=' <-> ')
            current = current.next
        print('null')

# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.insert(20, 1)
    dll.insert(5, 1)
    dll.append(30)
    dll.append(40)
    dll.append(50)

    print("List:", dll)
    print("Value at index 3:", dll.get(3))
    dll.traverse()  # prints: 10 <-> 5 <-> 20 <-> 30 <-> 40 <-> 50 <-> null
