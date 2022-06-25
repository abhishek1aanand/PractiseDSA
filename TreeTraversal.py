''' Tree traversal in python '''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.data) + "->", end='')
        # Traverse right
        inorder(root.right)


def preorder(root):
    if root:
        # Traverse root
        print(str(root.data) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


def postorder(root):
    if root:
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)
        # Traverse root
        print(str(root.data) + "->", end='')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal")
inorder(root)

print("\nPreorder traversal")
preorder(root)

print("\nPostorder traversal")
postorder(root)



