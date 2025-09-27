from linkedlist import *
def merging_ll(head_list1,head2_list):
    if head_list1 is None:
        return head2_list
    if head2_list  is None:
        return head_list1
    #the above part is done in order to return one list if another is empty
    final_head = None
    final_Tail = None#initialize both of these values as None

    while head_list1 is not None and head2_list is not None:#this part keeps the loop moving
        # head_list1=[3,5,7,12,54],head2_list= [1,2,5,10]
        if head_list1.data < head2_list.data:#this part will compare the two lists' data
            if final_head is None:
                final_head = head_list1
                final_Tail = head_list1
            else:
                final_Tail.next = head_list1
                final_Tail = head_list1
            head_list1 = head_list1.next
        else:
            if final_head is None:
                final_head = head2_list
                final_Tail = head2_list
            else:
                final_Tail.next = head2_list
                final_Tail = head2_list
            head2_list = head2_list.next
    if head_list1 is not None:
        final_Tail.next = head_list1
    if head2_list is not None:
        final_Tail.next = head2_list
    return final_head

def reverse_LL_Better(head):
    # Base Case
    # print_LL(head)
    if head is None or head.next is None: # First always head is None
        return head

    smallLinkedListHead = reverse_LL_Better(head.next)

    tailOfReversedList = head.next
    tailOfReversedList.next = head
    head.next = None

    return smallLinkedListHead
heady1 = take_input([3,5,7,12,54])
final  =  reverse_LL_Better(head=heady1)
printLL(final)
