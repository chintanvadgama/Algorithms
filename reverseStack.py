# Reverse Stack

class Stack:
	def __init__(self):
		self.stack = []
	def push(self,item):
		self.stack.append(item)
	def isEmpty(self):
		if self.stack:
			return False
		else:
			return True
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[len(self.stack)-1]
	def size(self):
		return len(self.stack)