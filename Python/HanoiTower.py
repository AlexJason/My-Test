# HanoiTower.py
# Alex Cui
# 2018/8/5

from PyStack import Stack
from datetime import datetime

time = 0

def HanoiTower(n, a, b, c):
	global time
	if n == 0:
		return
	HanoiTower(n-1, a, c, b)
	c.push(a.pop())
	time += 1
	HanoiTower(n-1, b, a, c)

def main():
	count = 24
	a = Stack()
	b = Stack()
	c = Stack()

	for i in range(count):
		a.push(count - i)

	print('After Init:')
	print(a)
	print(b)
	print(c)

	start = datetime.now()
	HanoiTower(count, a, b, c)
	end = datetime.now()

	print('After Move:')
	print(a)
	print(b)
	print(c)

	print('Time:', end - start)
	print('Move:', time)

if __name__ == '__main__':
	main()
