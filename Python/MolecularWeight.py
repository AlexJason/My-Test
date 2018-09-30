# MolecularWeight.py

def main():
	H = int(input('Count of H:'))
	C = int(input('Count of C:'))
	O = int(input('Count of O:'))

	molecular = H*1.00794 + C*12.0107 + O*15.9994
	print('Molecular: %f g/mol'%molecular)

	input('Press <Enter> to continue...')
	return 0

main()
