# hypotenuse.py

import math

def rad(deg):
	return math.pi * deg / 180

def main():
	a = float(input('Angle:'))
	h = float(input('Height:'))
	l = h / math.sin(rad(a))
	print('Hypotenuse:', l)
	
	input('Press <Enter> to continue...')
	return 0

main()
