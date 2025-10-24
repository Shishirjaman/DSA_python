class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "[" + ", ".join(values) + "]"

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None and _ != index-2:
                raise ValueError("Index out of bounds")
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def delete(self, value):
        if self.head is None:
            raise ValueError("Empty linked list")
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("Value not found")

    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise ValueError("Index out of bounds")
            current = current.next
        if current.next is None:
            raise ValueError("Index out of bounds")
        current.next = current.next.next

    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        current = self.head
        for _ in range(index):
            if current.next is None:
                raise ValueError("Index out of bounds")
            current = current.next
        return current.value
      
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("null")

    # Reverse the entire linked list in-place
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next     # Save the next node
            current.next = prev          # Reverse pointer
            prev = current               # Move prev forward
            current = next_node          # Move to next node
        self.head = prev
        
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next        # Move one step
            fast = fast.next.next   # Move two steps
        # Now slow points to the middle node
        if slow:
            return slow.value
        return None
    
    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                # Duplicate found: remove it
                prev.next = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10, 0)
    ll.insert(20, 1)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    print(ll)
    print(ll.get(4))
    ll.pop(4)
    print(ll)
    ll.delete(30)
    print(ll)
    
    ll.traverse()
    print(ll.find_middle())
    
    ll.append(20)
    ll.reverse()
    ll.traverse()
    ll.remove_duplicates()
    ll.traverse()
