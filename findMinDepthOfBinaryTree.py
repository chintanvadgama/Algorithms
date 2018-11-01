# find min depth of binary tree
class Node: 
	def __init__(self,root):
		self.root =root
		self.leftChild = None
		self.rightChild = None

def findMinDepth(root):
	q = [] # queue to keep the track of {'node':node,'depth':depth}
	q.append({'node':root,'depth':1})
	while (len(q)>1):
		item = q.pop()
		node = item['node']
		depth = item['depth']
		# No left or right child
		if node.leftChild is None and node.rightChild is None:
			return depth
		# if left child then append left child as node and increase depth by 1
		if node.leftChild is not None:
			q.append({'node':node.leftChild,'depth':depth+1})
		# if right child then append right child as node and increase depth by 1
		if node.rightChild is not None:
			q.append({'node':node.rightChild,'depth':depth+1})


