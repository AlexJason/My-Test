# CHelloWorld.py
from ctypes import *

def main():
	msvcrt = cdll.msvcrt
	msgstr = "Hello world!\n"
	msvcrt.wprintf("MSVCRT: %s", msgstr)

	input('Press <Enter> to continue...')
	return 0

main()
