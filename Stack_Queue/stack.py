#implementing Stack in python

#Creating a stack
def create_stack():
    stack = []
    return stack


#checking a stack is empty or not
def check_empty(stack):
    return len(stack) == 0


#adding item into the stack
def push(stack, item):
    stack.append(item)

    print(f'pushed item: {item}')

    return stack



#Removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"

    return stack.pop()



if __name__=="__main__":

    storage = create_stack()

    storage = push(storage, str(5))
    storage = push(storage, str(4))
    storage = push(storage, str(3))
    storage = push(storage, str(1))

    print(f'the stack: {storage}')

    print(f'popped item:  {pop(storage)}')

    print(f'stack after popping element: {storage}')
    
