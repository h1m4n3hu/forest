class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def rev_lev_ord(self):
        l=[]
        ll=[]
        k=self.head
        l.append(k)
        while l:
            k=l.pop(0)
            ll.append(k.value,end=" ")
            if k.right:
                l.append(k.right)
            if k.left:
                l.append(k.left)
        for i in reversed(ll):
            print(i)


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.rev_lev_ord()

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7