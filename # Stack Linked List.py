# Stack Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        poppedData = self.head.data
        self.head = self.head.next
        return poppedData
    
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data
    
linked_list_stack = linkedListStack()
linked_list_stack.push(1)
linked_list_stack.push(2)
linked_list_stack.push(3)

print("Peek:", linked_list_stack.peek())  
print("Pop:",  linked_list_stack.pop())    
print("Pop:", linked_list_stack.pop())    
print("Is Empty:", linked_list_stack.is_empty())