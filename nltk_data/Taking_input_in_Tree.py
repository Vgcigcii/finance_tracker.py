from Trees import Trees,print_tree_details,generic_tree
from collections import deque

# queue = deque([1,2,3])
def take_input():
    # first ask for data in the first node
    data = int(input("Enter the root data:\n"))
    # then make it a root using trees clas
    root = Trees(data)
    #then make this into a queue in which data can be added and removed from both ends
    queue = deque([root])
    while len(queue)!= 0:
        current_node = queue.popleft()
        num_children = int(input(f"Enter the number of children for {str(current_node.data)}:\n"))

        for i in range(num_children):
            child_data = int(input(f"enter the data for  child {i+1} of node{current_node.data}:\n"))
            child_node = Trees(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

# root = take_input()
# print_tree_details(root)
#Count number of nodes
def count_nodes(root):
    if root is None:
        return 0
    number_of_Nodes = 1
    for eachChild in root.children:
        number_of_Nodes = number_of_Nodes+count_nodes(eachChild)
    return number_of_Nodes
root1,root2 = generic_tree()
print(count_nodes(root1))
print(count_nodes(root2))

#Height of tree
# it just means how many levels there are in a tree
#        1----> height = 1
#       / \
#      2   3----> height = 2
#     / \ / \
#     4 5 6  7---->height = 3