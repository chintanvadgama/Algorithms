# Implement a queue and solve hotpotato/musical chair problem

class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		if self.items:
			return False
		else:
			return True
	def size(self):
		return len(self.items)

	def printqueue(self):
		return self.items

def hotPotato(names,num):
	q = Queue()
	for name in names:
		q.enqueue(name)
	print q.printqueue()

	while q.size() > 1:
		for i in range(num):
			q.enqueue(q.dequeue())
			print 'after enqueue', q.printqueue()
		q.dequeue()

	return q.dequeue()


if __name__ == '__main__':
	print hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)