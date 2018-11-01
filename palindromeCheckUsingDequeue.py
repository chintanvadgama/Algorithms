# Palindrome checker using Dequeue
# Double ended queue
class DeQueue:
	def __init__(self):
		self.items = []
	def addFront(self,item):
		self.items.append(item)
	def addRear(self,item):
		self.items.insert(0,item)
	def removeFront(self):
		return self.items.pop()
	def removeRear(self):
		return self.items.pop(0)
	def isEmpty(self):
		if self.items:
			return False
		else:
			return True
	def __repr__(self):
		print self.items
	def size(self):
		return len(self.items)


def checkPalindrome(string):
	chq = DeQueue()
	for s in string:
		chq.addRear(s)
	chq.__repr__()
	palindrome = True
	while chq.size() > 1 and palindrome:
		front = chq.removeFront()
		rear = chq.removeRear()
		if front != rear:
			palindrome = False
	return palindrome

if __name__ == '__main__':
	print checkPalindrome('radar')
	print checkPalindrome('toot')
	print checkPalindrome('chintan')

