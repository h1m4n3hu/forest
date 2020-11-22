class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def morris_postord(self):
        k=self.head
        while k:
            if k.right:
                pre=k.right
                while pre.left and pre.left!=k:
                    pre=pre.left
                if pre.left is None:
                    yield k.value
                    pre.left=k
                    k=k.right
                else:
                    pre.left=None
                    k=k.left
            else:
                yield k.value
                k=k.left


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
for i in reversed(list(t.morris_postord())):
    print(i,end=" ")

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7