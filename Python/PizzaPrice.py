# PizzaPrice.py

import math

def main():
	r = float(input('Input the d(cm):')) / 2
	p = float(input('Input the price($/cm2):'))
	total = math.pi * (r ** 2) * p
	print('The price is: $ ', round(total, 2))

	input('Press <Enter> to continue...')
	return 0

main()
