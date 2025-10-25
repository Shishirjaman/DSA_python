class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.value))
            current = current.next
        return "[" + ", ".join(items) + "]"

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_value

    def peek(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        return self.front.value


    def min(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        min_value = self.front.value
        current = self.front.next
        while current:
            if current.value < min_value:
                min_value = current.value
            current = current.next
        return min_value

    def max(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        max_value = self.front.value
        current = self.front.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    def search(self, value):
        position = 0
        current = self.front
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.front
        self.rear = self.front  # Will be updated to new rear after reversal
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.front = prev

    def sort(self):
        # Extract all values to a list
        values = []
        current = self.front
        while current:
            values.append(current.value)
            current = current.next
        values.sort()
        # Rebuild the queue
        self.front = self.rear = None
        self.size = 0
        for val in values:
            self.enqueue(val)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(30)
    queue.enqueue(20)

    print("Queue:", queue)                      # [10, 40, 50, 30, 20]
    print("Min:", queue.min())                  # 10
    print("Max:", queue.max())                  # 50
    print("Search 30:", queue.search(30))       # 3
    print("Search 99:", queue.search(99))       # -1

    print("\nReversing queue...")
    queue.reverse()
    print("Queue after reverse:", queue)        # [20, 30, 50, 40, 10]

    print("\nSorting queue...")
    queue.sort()
    print("Queue after sort:", queue)           # [10, 20, 30, 40, 50]
