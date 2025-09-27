from collections import deque
class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def taking_input_level_wise():
    data = int(input("Please enter the input :\n"))
    if data == -1:
        return None
    root = Binary_Tree(data)
    queue = deque([root])
    while len(queue)!=0:
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter left child for {current_node.data}:\n"))
        if left_child_data!=-1:
            left_node = Binary_Tree(left_child_data)
            current_node.left = left_node
            queue.append(left_node)
        right_child_data = int(input(f"Enter right child for {current_node.data}:\n"))
        if right_child_data!=-1:
            right_node = Binary_Tree(right_child_data)
            current_node.right = right_node
            queue.append(right_node)
    return root
def diameter_of_binary_tree(root):
    if root is None:
        return 0,0
    left_height,left_diameter = diameter_of_binary_tree(root.left)
    right_height,right_diameter = diameter_of_binary_tree(root.right)
    diameter_through_root = 1+left_diameter+right_diameter
    ans_diameter = max(diameter_through_root,left_diameter,right_diameter)
    current_tree_height= 1+max(left_height,right_height)
    return current_tree_height,ans_diameter
def print_binary_tree_level_wise(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            print(f"{current_node.data}:",end=",")
            if current_node.left is not None:
                print(f"Left->{current_node.left.data}",end = ",")
                queue.append(current_node.left)
            else:
                print("Left->None",end=",")
            if current_node.right is not None:
                print(f"Right -> {current_node.right.data}",end=" ")
                print()
                queue.append(current_node.right)
            else:
                print("Right->None",end = " ")
        print()

base_root=taking_input_level_wise()
print(diameter_of_binary_tree(base_root))
