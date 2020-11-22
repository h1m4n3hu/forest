class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def stepped_inwards(self):
        k=self.head
        l1=[]
        m=k.left
        l2=[]
        n=k.right
        print(k.value)
        l1.append(m)
        l2.append(n)
        while l1 or l2:
            mm=l1.pop(0)
            nn=l2.pop(0)
            print(mm.value)
            print(nn.value)
            if mm.left:l1.append(mm.left)
            if nn.left:l2.append(nn.right)
            if mm.right:l1.append(mm.right)
            if nn.right:l2.append(nn.left)


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.stepped_inwards()

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7