# PyStack.py
# Alex Cui
# 2018/8/5

class Stack(object):
	def __init__(self):
		self.list = list()

	def __str__(self):
		return str(self.list)

	def is_empty(self):
		return self.list == []

	def peek(self):
		return self.list[-1]

	def size(self):
		return len(self.list)

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()
