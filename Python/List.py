class Node():
	def __init__(self, value=None):
		self.value = value
		self.last = None
		self.next = None

	def __repr__(self):
		return self.value

class List():
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	def __getitem__(self, index):
		if index >= self.__size or index < -self.__size:
			raise IndexError("Index out of subrange.")
		if index < 0:
			p = self.__tail
			for i in range(abs(index) - 1):
				p = p.last
			return p
		else:
			p = self.__head
			for i in range(index):
				p = p.next
			return p

	def __setitem__(self, index, item):
		if index >= self.__size or index < -self.__size:
			raise IndexError("Index out of subrange.")
		if index < 0:
			p = self.__tail
			for i in range(abs(index) - 1):
				p = p.last
			p.value = item
		else:
			p = self.__head
			for i in range(index):
				p = p.next
			p.value = item

	def __repr__(self):
		string = '[Size]%d\n'%(self.__size)
		p = self.__head
		for i in range(self.__size):
			string += '[%d]%s\n'%(i, str(p.value))
			p = p.next
		return string

	def empty(self):
		return __size == 0

	def push_back(self, item):
		if self.__head == None:
			self.__head = Node(value=item)
			self.__tail = self.__head
		else:
			self.__tail.next = Node(value=item)
			self.__tail.next.last = self.__tail
			self.__tail = self.__tail.next
		self.__size += 1

	def erase(self, index):
		p = self.__getitem__(index)
		if p == self.__head:
			self.__head = p.next
		elif p == self.__tail:
			self.__tail = p.last
		else:
			p.last.next = p.next
			p.next.last = p.last
		self.__size -= 1

	def insert(self, index, item):
		if index == self.__size:
			self.push_back(item)
		else:
			p = self.__getitem__(index)
			if p == self.__head:
				p.last = Node(value=item)
				p.last.next = p
				self.__head = p.last
			else:
				node = Node(value=item)
				node.last = p.last
				p.last.next = node
				node.next = p
				p.last = node
			self.__size += 1

	def swap(self, index0, index1):
		if index0 < 0:
			index0 = self.__size - index0 * (-1)
		if index1 < 0:
			index1 = self.__size - index1 * (-1)
		if index0 == index1:
			return
		if index0 > index1:
			index0, index1 = index1, index0
		p = self.__getitem__(index0)
		q = self.__getitem__(index1)
		if p.next == q:
			if p == self.__head:
				p.next.last = q
				p.next = q.next
				p.last = q
				q.last = p.last
				q.next = p
				self.__head = q
				p.next = q.next.next
			p.last.next = q
			q.next.last = p
			p.next = q.next
			p.last = q
			q.last = p.last
			q.next = p
		else:
			p.last.next = q
			p.next.last = q
			q.next.last = p
			q.last.next = p
			p.next = q.next
			p.last = q.last
			q.next = p.next
			q.last = p.last


def main():
	l = List()
	l.push_back(1)
	l.push_back(2)
	l.push_back(3)
	l.push_back(4)
	l.insert(3, 3.5)
#	l.swap(1, 2)
	l.swap(0, 1)
	print(l)

if __name__ == '__main__':
	main()

