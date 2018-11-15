#Binary tree in python
class BinaryTree:
	def __init__(self,root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode) # Newnode binary tree object
			t.leftChild = self.leftChild #current left child of tree to be pushed down
			self.leftChild = t #new binary tree object becomes left child

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def getRoot(self):
		return self.key

	def setRoot(self,root):
		self.key = root
