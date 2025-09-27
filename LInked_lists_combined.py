from linkedlist import Node
class LinkedList:
    def __init__(self):
        self.head= None
    def insertAtHead(self,data):
        new_Node = Node(data)  # this New node will store the value added by the user
        new_Node.next = self.head  # this step will point towards the location of old ll it can be 10->20->30
        self.head = new_Node  # now this step will join the old data to the new data
        return self.head
    def insertAtTail(self,data):
        new_Node = Node(data)
        if self.head is None:
            return new_Node
        self.head.next  = self.insertAtTail(self.head.next,data)
        return self.head
    def print_my_LL(self,head):
        if head is None:
            return
        print(head.data, end="->")
        return self.print_my_LL(head.next)

linked_list_output = LinkedList()
linked_list_output.insertAtHead(data=10)
linked_list_output.insertAtHead(data=10)
linked_list_output.insertAtHead(data=10)
linked_list_output.insertAtHead(data=10)
linked_list_output.print_my_LL(linked_list_output.head)
