# Python program for postorder traversals

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print postorder traversal
def printPostorder(node):
    if node is None:
        return


    # Recur on left subtree
    printPostorder(node.left)

    # Recur on right subtree
    printPostorder(node.right)

    # Deal with the node
    print(node.data, end=' ')


# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Postorder traversal of binary tree is:")
    printPostorder(root)