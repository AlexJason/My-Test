# Eight queen problem
# Alex Cui
# 2018/7/19

from functools import *

def NQueen(n, ln=[], i=1, m=0):
	return [[(int(bool(sum(l))) if i==(n-1) else sum([NQueen(n, nl, i+1, x) for x in range(n) if l[x]])) \
		for l in [reduce(lambda x,y:[x[a] and y[a] for a in range(len(x))], [[True for x in range(n)]]+[ \
		[False if x==nl[k] or x==nl[k]-(i-k) or x==nl[k]+(i-k) else True for x in range(n)] for k in  \
		range(i)])]][0] for nl in [[m if x==i-1 else ln[x] for x in range(len(ln))]]][0] if len(ln)==n \
		else sum([NQueen(n, [0]*n, 1, i) for i in range(n)])

'''
def NQueen(n):
	line = [0]*n
	c = 0
	for i in range(n):
		line[0] = i;
		c += next(line, 1, n)
	return c

def next(line, n, ln):
	c = 0
	thisline = [True]*ln
	for i in range(n):
		thisline[line[i]] = False
		if line[i]+(n-i) < ln:
			thisline[line[i]+(n-i)] = False
		if line[i]-(n-i) >= 0:
			thisline[line[i]-(n-i)] = False
	if n == ln-1:
		return sum(thisline)
	for i in range(len(thisline)):
		if thisline[i]:
			line[n] = i
			c += next(line, n + 1, ln)
	return c
'''
def main():
	print(NQueen(10))
#	print(NQueen(10))

if __name__ == '__main__':
	main()
