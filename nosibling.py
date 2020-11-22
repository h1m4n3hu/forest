class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def nosibling(self,head):
        if head:
            if head.left and not head.right:
                print(head.left.value)
            if head.right and not head.left:
                print(head.right.value)
            self.nosibling(head.left)
            self.nosibling(head.right)


t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.nosibling(t.head)

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7