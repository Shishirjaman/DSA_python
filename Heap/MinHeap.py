class MinHeap:
    """A classic binary min heap with (key, value) pairs."""

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

    def peek_min(self):
        """Return the minimum (key, value) pair without removing."""
        if not self.heap:
            raise IndexError("Empty heap")
        return self.heap[0]

    def extract_min(self):
        """Remove and return the minimum element."""
        if not self.heap:
            raise IndexError("Empty heap")
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._shift_down(0)
        return min_element

    def heapify(self, elements):
        """Build a heap from an initial list of (key, value) pairs."""
        self.heap = list(elements)
        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._shift_down(i)

    def meld(self, other_heap):
        """Combine with another heap and re-heapify."""
        self.heap.extend(other_heap.heap)
        self.heapify(self.heap)
        other_heap.heap.clear()  # Clear the OTHER heap

    def _parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    def _left(self, index):
        l = 2 * index + 1
        return l if l < len(self.heap) else None

    def _right(self, index):
        r = 2 * index + 2
        return r if r < len(self.heap) else None

    def _shift_up(self, index):
        parent = self._parent(index)
        while parent is not None and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def _shift_down(self, index):
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def is_empty(self):
        return len(self.heap) == 0

    def replace_min(self, key, value):
        if self.is_empty():
            self.insert(key, value)
        else:
            min_element = self.heap[0]
            self.heap[0] = (key, value)
            self._shift_down(0)
            return min_element

    def min_value(self):
        if self.is_empty():
            raise IndexError("Empty heap")
        return self.heap[0][1]

    def contains(self, key):
        return any(k == key for k, _ in self.heap)

if __name__ == "__main__":
    heap = MinHeap()
    heap.heapify([[10, 'A'], [9, 'B'], [8, 'C'], [7, 'D'], [6, 'E'],
                  [5, 'F'], [4, 'G'], [3, 'H'], [2, 'I'], [1, 'J']])
    print("Heap:", heap)
    print("Min item:", heap.peek_min())         # (1, 'J')
    print("Extracting min:", heap.extract_min())# (1, 'J')
    print("Heap after extraction:", heap)
    heap.insert(0, 'Z')
    print("Heap after inserting (0, 'Z'):", heap)
    
    print("Is the heap empty?", heap.is_empty())  # Should be False

    print("The value of min key:", heap.min_value())  # Should be 'J' (key 1)

    print("Heap contains key 3?", heap.contains(3))   # Should be True
    print("Heap contains key 99?", heap.contains(99)) # Should be False

    old_min = heap.replace_min(0, 'Z')
    print("Old min extracted by replace_min:", old_min)  # Should be (1, 'J')
    print("Heap after replace_min (0, 'Z'):", heap)
    print("Current min:", heap.peek_min())  # Should be (0, 'Z')
