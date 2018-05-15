# quadratic.py

import math

def main():
	print('Input the ax^2+bx+c=0')

	a = float(input('a:'))
	b = float(input('b:'))
	c = float(input('c:'))

	delta = b**2 - 4*a*c

	if delta < 0:
		print('No solutions.')
		return -1
	elif delta == 0:
		root = (-b)/(2*a)
		print('Solutions: x1=%lf, x2=%lf'%(root, root))
	else:
		root1 = (-b + math.sqrt(delta))/(2*a)
		root2 = (-b - math.sqrt(delta))/(2*a)
		print('Solutions: x1=%lf, x2=%lf'%(root1, root2))

	input('Press <Enter> to continue...')
	return 0

main()
