class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def spiral(self):
        s1=[]
        s2=[]
        s1.append(self.head)
        while s1 or s2:
            while s1:
                k=s1.pop()
                print(k.value,end=" ")
                if k.right:s2.append(k.right)
                if k.left:s2.append(k.left)
            print("\n")
            while s2:
                k=s2.pop()
                print(k.value,end=" ")
                if k.left:s1.append(k.left)
                if k.right:s1.append(k.right)
            print("\n")


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.spiral()

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7