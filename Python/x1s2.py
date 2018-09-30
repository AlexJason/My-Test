# x1s2.py
import re

class Node(object):
	def __init__(self, left=0, mark='+', right=0):
		self.left = left
		self.right = right
		self.mark = mark

	def __str__(self):
		return '(' + str(self.left) + self.mark + str(self.right) + ')'

def solve_x(a, b=0, c=0):
	if a == 0:
		raise ValueError('a cannot be zero.')
	delta = b**2 - 4*a*c
	if delta >= 0:
		x1 = ((-b) + delta**(0.5)) / (2*a)
		x2 = ((-b) - delta**(0.5)) / (2*a)
		return [x1, x2]
	else:
		raise ValueError('No such solution.')
	return

def solve_s(s, var='x'):
	tsx = s.replace(var, 'x')
	tsx = tsx.replace('^', '**')
	tsx = tsx.replace('xx', 'x**2')
	tsx = tsx.replace('x*x', 'x**2')
	tsy = tsx.replace('x**2', 'y') # ax**2 + bx + c => ay + bx +c
	tsy = re.sub(r'(\d(\.\d){0,1})([xy])', r'(\1*\3)', tsy) # ax => (a*x)
	tsy = tsy.replace('=', '-(')+')' # TO=> ax**2 + bx + c = 0
	print(tsy)
	c = cut(tsy)
	print(c)

def cut(s):
	level = 0
	print('Debug:'+s)
	if re.match(r'(\d(\.\d){0,1}|[xy])[\+\-\*\/](\d(\.\d){0,1}|[xy])', s):
		ts = re.sub(r'(\d(\.\d){0,1}|[xy])([\+\-\*\/])(\d(\.\d){0,1}|[xy])', r'\1@\3@\4', s)
		ts = ts.split('@')
		return Node(left=ts[0], mark=ts[1], right=ts[2])
	s = re.sub(r'(\d(\.\d){0,1})([\*])\((\d(\.\d){0,1}|[xy])([\+\-])(\d(\.\d){0,1}|[xy])\)', r'((\1\3\4)\6(\1\3\7))', s)
	s = re.sub(r'(\d(\.\d){0,1})([\*])\((\(.*\))([\+\-])(\(.*\))\)', r'((\1\3\4)\5(\1\3\6))', s)
	s = re.sub(r'\((\d(\.\d){0,1}|[xy])([\+\-])(\d(\.\d){0,1}|[xy])\)([\*\/])(\d(\.\d){0,1})', r'((\1\6\4)\3(\1\6\7))', s)
	for i in range(len(s)):
		if s[i] == '(':
			level += 1
		elif s[i] == ')':
			level -= 1
		if level == 0 and (s[i] in ['+', '-']):
			return Node(left=cut(s[:i]), mark=s[i], right=cut(s[i+1:]))
	return None

if __name__ == '__main__':
	s = '4*(x^2+3)*3-5*x+(3-x)=3*x'
	print(s)
	solve_s(s)

