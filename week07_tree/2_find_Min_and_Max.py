#   2 หาค่า Min และ Max
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            now = self.root
            while True:
                if data < now.data:
                    if now.left == None:
                        now.left = Node(data)
                        break
                    else:
                        now = now.left
                else:
                    if now.right == None:
                        now.right = Node(data)
                        break
                    else:
                        now = now.right
        return self.root

    def findMin(self):
        if self.root == None:
            return -1
        else:
            now = self.root
            while now.left is not None:
                now = now.left
            return now.data
        
    def findMax(self):
        if self.root == None:
            return -1
        else:
            now = self.root
            while now.right is not None:
                now = now.right
            return now.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min : {}".format(T.findMin()))
print("Max : {}".format(T.findMax()))