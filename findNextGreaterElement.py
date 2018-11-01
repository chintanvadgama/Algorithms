# Find a next greater element in arrary and if not exists then return -1
# 2 ways 
# 1. using 2 for loops
# 2. using stack
# [15,2,9,10] 
# 15 --> -1
# 2 --> 9
# 9 --> 10
# 10 --> -1

# 1. using 2 for loops
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

def find_next_great_ele(arr):
	if arr:
		for i in range(0,len(arr),1):
			next_element = -1
			for j in range(i+1,len(arr),1):
				# print 'arr[i] = %s, arr[j] = %s' %(arr[i],arr[j])
				if arr[i] < arr[j]:
					next_element =arr[j]
					break
			print '%s ---> %s' %(arr[i],next_element)

def find_next_grt_ele_stack(arr):
	s = Stack()
	# push the 1st ele to stack
	s.push(arr[0])
	for i in range(0,len(arr),1):
		# assume the element is arr[i]
		next_ele = arr[i]
		if s.isEmpty() == False:
			element = s.pop()
			while element < next_ele:
				print '%s --> %s' %(element,next_ele)
				if s.isEmpty() == True:
					break
				element = s.pop()
			if element > next_ele:
				s.push(element)
		s.push(next_ele)
	while(s.isEmpty()==False):
		element = s.pop()
		print '%s --> -1' % element


if __name__ == '__main__':
	find_next_great_ele([15,2,9,10])
	find_next_grt_ele_stack([15,2,9,10])
