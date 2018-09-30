from ctypes import *

def main():
	msvcrt = cdll.msvcrt
	msg_str = 'Hello world!\n'
	msvcrt.wprintf('Testing: %s', msg_str)

if __name__ == '__main__':
	main()
