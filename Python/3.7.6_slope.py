# slope.py

class point():
	x = float()
	y = float()
	def __init__(self):
		self.x = 0
		self.y = 0

def main():
	p1 = point()
	p2 = point()
	p1.x = float(input('Input x of point1:'))
	p1.y = float(input('Input y of point1:'))
	p2.x = float(input('Input x of point2:'))
	p2.y = float(input('Input y of point2:'))
	try:
		k = (p2.y - p1.y) / (p2.x - p1.x)
		print('slope = ', k)
	except ZeroDivisionError as e:
		print('slope is non-existent.')

	input('Press <Enter> to continue...')
	return 0

main()
