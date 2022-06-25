class Node:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None


def inorderTraversal(root):
    if root is not None:
        # Traverse left
        inorderTraversal(root.left)

        # Traverse root
        print(str(root.key) + "->", end =' ')

        # Traverse right
        inorderTraversal(root.right)


# Insert in a node:
def insert(node, key):
    if node is None:
        return  Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def deleteNode(root, key):



root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorderTraversal(root)
