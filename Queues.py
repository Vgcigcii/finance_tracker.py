from networkx.classes import is_empty
from sympy.codegen.cnodes import sizeof


class Queues_using_List:
    def __init__(self):
        self.__queue = []
    def size_queue(self):
        return len(self.__queue)
    def is_empty_queue(self):
        return len(self.__queue)==0
    def front_element_queue(self):
        return self.__queue[0]
    def enqueue_to_queue(self,data):
        return self.__queue.append(data)
    def dequeue_to_queue(self):
        return  self.__queue.pop(0)
    def show_queue(self):
        return self.__queue

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queues_using_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    def size_queue(self):
        return self.len
    def is_empty(self):
        return self.size_queue() == 0
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.head.data
    def enqueue(self,data):
        new_value = Node(data)
        self.len+=1
        if self.head is None:
            self.head = new_value
            self.tail = new_value
        else:
            self.tail.next = new_value
            self.tail = new_value
        return self.head.data
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        self.len-=1
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return self.head.data
    def show_elements(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.head
        elements = []
        while temp is not None:
            elements.append(temp.data)
            temp = temp.next
        return elements


practice_queue = queues_using_LL()
print(practice_queue.is_empty())
practice_queue.enqueue(10)
practice_queue.enqueue(20)
practice_queue.enqueue(30)
practice_queue.enqueue(40)
print(practice_queue.is_empty())
print(practice_queue.size_queue())
print(practice_queue.front())
print(practice_queue.dequeue())
print(practice_queue.show_elements())