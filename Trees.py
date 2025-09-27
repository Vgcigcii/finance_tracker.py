from collections import deque


class Trees:
    def __init__(self,data):
        self.data = data
        self.children =[]

def take_input_level_wise():
    root_Node = int(input("Please enter the root value(-1 to exit):\n"))
    if root_Node==-1:
        return
    first_node = Trees(root_Node)
    root_holder = deque([first_node])
    while root_holder:
        current_element = root_holder.popleft()
        num_children = int(input(f"Please enter the number of children in {str(current_element.data)}:\n"))
        for i in range(num_children):
            child_data = int(input(f"Enter the data for  child {i+1} of {current_element.data}:"))
            child_node = Trees(child_data)
            current_element.children.append(child_node)
            root_holder.append(child_node)
    return  first_node
root = take_input_level_wise()
def height_of_tree(root_node):
    if root_node is None:
        return 0
    max_height = 0
    for eachChild in root_node.children:
        max_height = max(max_height,height_of_tree(eachChild))
    final_height = 1+max_height
    return final_height
print(f"The height of tree is {height_of_tree(root)}")