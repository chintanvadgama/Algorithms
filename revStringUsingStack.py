# Reverse string using Stack

# 1. Implement a stack class
# 2. Use the stack to reverse string


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


def rev_string(string):
	s = Stack()
	if string:
		for i in range(len(string)):
			s.push(string[i])
	rev_string = ''
	for i in range(len(string)):
		rev_string += s.pop()
	return rev_string

if __name__ == '__main__':
	name = 'chintan'
	print rev_string(name)


