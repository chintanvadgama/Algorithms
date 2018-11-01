# 4 ways
# 1. Node
# 2. left + root
# 3. right + root
# 4. Left + node + max through the right path
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def findMaxPath(root):
	if root is None:
		return 0

	l = findMaxPath(root.left)
	r = findMaxPath(root.right)
	# maximum of 1. max(left or right) + root  OR 2.root itself
	max_single = max(max(l,r)+root.data,root.data)

	max_top = max(max_single,l+r+root.data)

	# static variable to store the result
	findMaxPath.res = max(findMaxPath.res,max_top)

	return max_single

def findMaxSum(root):
	findMaxPath.res = float('-inf')
	findMaxPath(root)
	return findMaxPath.res


