# AreaTriangle.py

import math

class Triangle():
	a = float()
	b = float()
	c = float()
	def __init__(self):
		self.a = 0.0
		self.b = 0.0
		self.c = 0.0
	def area(self):
		p = (self.a+self.b+self.c)/2
		S = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
		return S

def main():
	tri = Triangle()
	tri.a = float(input('Input a:'))
	tri.b = float(input('Input b:'))
	tri.c = float(input('Input c:'))
	print('Area:', tri.area())

	input('Press <Enter> to continue...')
	return 0

main()
