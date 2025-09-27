#Linked List
#Structure
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
print()
def take_input(values):
    head = None
    tail = None# first initialize both head and tail as None
    for value in values:
        new_node = Node(value)#initialize the new values as new node so it gets the value of the class Node
        if head is None:#this condition will definitely run
            head = new_node
            tail = new_node
        else:#then in the second iteration as head is not none anymore tail will be given the value and location of next in line
            tail.next = new_node
            tail = new_node
    return head
def printLL(printing_head):
    if printing_head is None:
        return
    print(printing_head.data,end="->")
    return printLL(printing_head.next)
# Calculating the length of a linked list
def length_ll(linked_head):
    if linked_head is None:
        return 0
    return 1+length_ll(linked_head.next)
 # print("before insertion")
def insertAtHead(old_head,data):
    new_head = Node(data)
    new_head.next  = old_head
    return new_head


