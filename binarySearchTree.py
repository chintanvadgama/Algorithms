class Node:
    def __init__(self,val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if self.value == data:
            return False

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            return self.root.insert(data)
