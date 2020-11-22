class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def preorder_traversal(self,start):
        if start:
            print(start.value,end=" ")               #current node
            self.preorder_traversal(start.left)      #left tree
            self.preorder_traversal(start.right)     #right tree

    def inorder_traversal(self,start):
        if start:
            self.inorder_traversal(start.left)       #left tree
            print(start.value,end=" ")               #current node
            self.inorder_traversal(start.right)      #right tree

    def postorder_traversal(self,start):
        if start:
            self.postorder_traversal(start.left)     #left tree
            self.postorder_traversal(start.right)    #right tree
            print(start.value,end=" ")               #current node


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.preorder_traversal(t.head)    #1 2 4 5 3 6 7 
t.inorder_traversal(t.head)     #4 2 5 1 6 3 7 
t.postorder_traversal(t.head)   #4 5 2 6 7 3 1 

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7