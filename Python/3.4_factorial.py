# factorial.py

def main():
	n = int(input('Please input a whole number(int):'))
	result = 1
	for i in range(1, n+1):
		result *= i
	print('The result is:', result)

	input('Press <Enter> to continue...')
	return 0

main()
