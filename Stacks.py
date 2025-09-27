class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        new_node = Node(data)
        self.size +=1
        if self.head is None:
            self.head = new_node
            return f"Added {data} to the stack"
        new_node.next = self.head
        self.head = new_node
        return f"Added {data} to the stack"

    def top(self):
        if self.head is None or self.size ==0:
            # raise IndexError()
            return "Stack is empty"
        return self.head.data

    def pop(self):
        if self.head is None or self.size == 0:
            # raise IndexError()
            return "Stack is empty,cannot pop"
        dataAtTop = self.head.data
        self.head = self.head.next
        self.size  -=1
        return dataAtTop

    def is_empty(self):
        return self.size == 0
    def size_stack(self):
        return self.size

myStack = StackUsingLL()
print(myStack.is_empty())
print(myStack.push(10))
print(myStack.push(20))
print(myStack.push(30))
print(myStack.push(40))
print(myStack.push(50))
print(myStack.is_empty())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.size_stack())
print(myStack.top())