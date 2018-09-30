# CStruct.py
from ctypes import *

class People(Structure):
	_fields_ = [
		("name", c_wchar_p),
		("age", c_uint),
		("male", c_bool),
	]

def main():
	p = People()
	p.name = c_wchar_p(input("Name:"))
	p.age = c_uint(int(input("Age:")))
	p.male = True if input("Sex:") == "m" else False
	print("==========")
	c = cdll.msvcrt
	c.wprintf("Name: %s, Age: %d, Male: %d\n", p.name, p.age, p.male)
	
	input('Press <Enter> to continue...')
	return 0

main()

