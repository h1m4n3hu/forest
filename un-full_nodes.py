class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.head=None


    def un_fulltree_nodes(self,head):
        if head:
            if not head.left and head.right or not head.right and head.left:
                print(head.value)   #nodes that have one child
            self.un_fulltree_nodes(head.left)
            self.un_fulltree_nodes(head.right)

t=Tree()
t.head=Node(1)
t.head.left=Node(2)
t.head.right=Node(3)
t.head.left.left=Node(4)
t.head.left.right=Node(5)
t.head.right.left=Node(6)
t.head.right.right=Node(7)
t.un_fulltree_nodes(t.head)

    #          1
    #         /  \
    #        /    \
    #       2      3
    #      / \    / \
    #     4   5  6   7