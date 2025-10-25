class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def __repr__(self):
        items = []
        current = self.top
        
        while current:
            items.append(str(current.value))
            current = current.next
            
        return "["+",".join(items)+"]"
    
    
    def __len__(self):
        return self.size
    
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
        self.size += 1
        
    
    def pop(self):
        if self.top is None:
            raise ValueError("Empty Stack")
        else:
            pop_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            
        return pop_value
    
    
    def peek(self):
        if self.top is None:
            raise ValueError("Empty Stack")
        
        return self.top.value
    
    
    def is_empty(self):
        return self.top is None
    
    
    def min(self):
        if self.is_empty():
            raise ValueError("Empty Stack")
        min_value = self.top.value
        current = self.top.next
        while current:
            if current.value < min_value:
                min_value = current.value
            current = current.next
        return min_value
    
    
    def max(self):
        if self.is_empty():
            raise ValueError("Empty Stack")
        max_value = self.top.value
        current = self.top.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
    
    
    def search(self, value):
        """Return the position from top (0-indexed) if found, else -1. O(n)"""
        current = self.top
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1
    
    
    def reverse(self):
        """Reverse the stack in-place. O(n)"""
        prev = None
        current = self.top
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev
        
        
    def sort(self):
        if self.is_empty():
            return
        # Use an auxiliary stack
        aux_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            # Move elements from aux_stack back to self if they're greater than temp
            while not aux_stack.is_empty() and aux_stack.peek() > temp:
                self.push(aux_stack.pop())
            aux_stack.push(temp)
        # Move sorted elements back to self
        while not aux_stack.is_empty():
            self.push(aux_stack.pop())


if __name__=="__main__":
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(5)
    stack.push(20)
    stack.push(15)

    print("Stack:", stack)           # [15, 20, 5, 30, 10]
    print("Min:", stack.min())       # 5
    print("Max:", stack.max())       # 30
    print("Search 20:", stack.search(20))  # 1 (position from top)
    print("Search 99:", stack.search(99))  # -1 (not found)

    print("\nReversing stack...")
    stack.reverse()
    print("Stack after reverse:", stack)  # [10, 30, 5, 20, 15]

    print("\nSorting stack...")
    stack.sort()
    print("Stack after sort:", stack) 