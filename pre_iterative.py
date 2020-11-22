class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def preorder_iter(self):
        l=[]
        l.append(self.head)
        while len(l)>0:
            node=l.pop()
            print(node.value,end=" ")
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.preorder_iter()

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7