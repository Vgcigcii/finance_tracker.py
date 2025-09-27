from linkedlist import Node, take_input, printLL


def insertAtHead(old_head,data):
    new_head = Node(data)
    new_head.next  = old_head
    return new_head
def insertAtTail(old_head,data):
    new_tail = Node(data)
    temp = old_head
    while temp.next is not None:
        temp= temp.next
    temp.next  = new_tail
    new_tail.next = None
    return old_head
# needs work
def insertAtIndex(old_head,new_data,index_added):
    data_to_be_added = Node(new_data)
    temp = old_head
    count = 0
    while temp.next is not None and count< index_added-1 :
        temp = temp.next
        count+=1
        if temp is None:
            print("Index out of bounds")
            return old_head
    data_to_be_added.next = temp.next
    temp.next = data_to_be_added
    return old_head
def deleteAtHead(old_head):
    if old_head is None:
        return None
    new_head = old_head.next
    return new_head

def deleteAtTail(old_head):
    if old_head is None:
        return None
    temp = old_head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return old_head
def deleteAtIndex(old_head,indexToDelete):
    counter = 0
    temp = old_head
    while counter< indexToDelete-1 and temp.next is not None:
        temp = temp.next
        counter+=1
    temp.next = temp.next.next
    return old_head
def deleteByValue(old_head,valueToDelete):
    if old_head is None:
        return  None
    if old_head.data is valueToDelete:
        return old_head.next
    temp = old_head
    while temp.next is not None:
        if temp.next.data is valueToDelete:
            temp.next = temp.next.next
            return old_head
        temp= temp.next
    return old_head
elements_ll = take_input([25,30,36])
v = insertAtHead(elements_ll,31)
c = insertAtTail(elements_ll,12)
b = insertAtIndex(elements_ll,21,2)
printLL(b)
print()
# x = elements_ll
# x = deleteAtHead(x)
# printLL(x)
# print()
# elements_ll = deleteAtTail(elements_ll)
# printLL(elements_ll)
# print()
elements_ll = deleteByValue(elements_ll,12)
printLL(elements_ll)
"""
let me think about that ....
i don't know much but i think we have to go through it with  a for  loop and then delete each occurrence
"""