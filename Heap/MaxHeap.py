class MaxHeap:
    """A classic binary max heap with (key, value) pairs."""

    def __init__(self):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def insert(self, key, value):
        """Insert a new (key, value) pair into the heap."""
        self.heap.append((key, value))
        self._shift_up(len(self.heap) - 1)

    def peek_max(self):
        """Return the maximum (key, value) pair without removing."""
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum element."""
        if not self.heap:
            raise IndexError("Empty heap")
        max_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._shift_down(0)
        return max_element

    def heapify(self, elements):
        """Build a heap from an initial list of (key, value) pairs."""
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._shift_down(i)

    def meld(self, other_heap):
        """Combine with another heap and re-heapify."""
        self.heap.extend(other_heap.heap)
        self.heapify(self.heap)
        other_heap.heap.clear()

    # Helper methods for index arithmetic
    def _parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    def _left(self, index):
        l = 2 * index + 1
        return l if l < len(self.heap) else None

    def _right(self, index):
        r = 2 * index + 2
        return r if r < len(self.heap) else None

    # "Swim"/"Bubble up" method for inserting
    def _shift_up(self, index):
        parent = self._parent(index)
        while parent is not None and self.heap[index][0] > self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    # "Sink"/"Bubble down" method for removing max
    def _shift_down(self, index):
        while True:
            largest = index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right is not None and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def is_empty(self):
        return len(self.heap) == 0

    def replace_max(self, key, value):
        if self.is_empty():
            self.insert(key, value)
            return None
        else:
            max_element = self.heap[0]
            self.heap[0] = (key, value)
            self._shift_down(0)
            return max_element

    def max_value(self):
        if self.is_empty():
            raise IndexError("Empty heap")
        return self.heap[0][1]

    def contains(self, key):
        return any(k == key for k, _ in self.heap)


if __name__ == "__main__":
    heap = MaxHeap()
    heap.heapify([
        (10, 'A'),
        (9, 'B'),
        (8, 'C'),
        (7, 'D'),
        (6, 'E'),
        (5, 'F'),
        (4, 'G'),
        (3, 'H'),
        (2, 'I'),
        (1, 'J')
    ])
    print("Heap:", heap)

    # Test is_empty
    print("Is the heap empty?", heap.is_empty())  # Should be False

    # Test max_value
    print("The value of max key:", heap.max_value())  # Should be 'A' (key 10)

    # Test contains (for present and absent keys)
    print("Heap contains key 8?", heap.contains(8))   # Should be True
    print("Heap contains key 99?", heap.contains(99)) # Should be False

    # Test replace_max
    old_max = heap.replace_max(20, 'Z')
    print("Old max extracted by replace_max:", old_max)  # Should be (10, 'A')
    print("Heap after replace_max (20, 'Z'):", heap)
    print("Current max:", heap.peek_max())  # Should be (20, 'Z')

    # Use extract_max to see it disappear
    print("Extract max:", heap.extract_max())  # Should be (20, 'Z')
    print("Heap after extract_max:", heap)

    # Test is_empty on an empty heap
    heap2 = MaxHeap()
    print("Is heap2 empty?", heap2.is_empty())  # Should be True
    try:
        heap2.max_value()
    except IndexError as e:
        print("max_value on empty heap2:", e)
