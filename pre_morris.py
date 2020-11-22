class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def morris_preord(self):
        k=self.head
        while k:
            if k.left:
                pre=k.left
                while pre.right and pre.right!=k:
                    pre=pre.right
                if pre.right is None:
                    print(k.value,end=" ")
                    pre.right=k
                    k=k.left
                else:
                    pre.right=None
                    k=k.right
            else:
                print(k.value,end=" ")
                k=k.right


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.morris_preord()

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7