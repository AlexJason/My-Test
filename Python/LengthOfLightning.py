# LengthOfLightning.py

def main():
	t = float(input('Time between lightning and thunder(s):'))
	l = 1100 * t / 5280
	# v = 1100ft/s
	# 1mile = 5280ft
	print('The length is: %f mile'%l)

	input('Press <Enter> to continue...')
	return 0

main()
