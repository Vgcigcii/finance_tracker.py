from Binary_trees import *
def preorder_binary_tree(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder_binary_tree(root.left)
    preorder_binary_tree(root.right)
def postorder_binary_tree(root):
    if root is None:
        return
    postorder_binary_tree(root.left)
    postorder_binary_tree(root.right)
    print(root.data, end=' ')
def inorder_binary_tree(root):
    if root is None:
        return
    inorder_binary_tree(root.left)
    print(root.data, end=' ')
    inorder_binary_tree(root.right)
preorder_binary_tree(base_root)
print()
postorder_binary_tree(base_root)
print()
inorder_binary_tree(base_root)