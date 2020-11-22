class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None
        self.num=0


    def levelof(self,root,val,lev=1):
        if root:
            if root.value==val:
                self.num+=lev
            self.levelof(root.left,val,lev+1)
            self.levelof(root.right,val,lev+1)
        return self.num


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
print(t.levelof(t.head,3))

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7