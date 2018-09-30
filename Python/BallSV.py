# BallSV.py

import math

def main():
	r = float(input('Input the R:'))
	V = (math.pi * (r ** 3) * 4) / 3
	S = 4 * math.pi * (r ** 2)
	print('V=', V, '\nS=', S)

	input('Press <Enter> to continue...')
	return 0

main()
