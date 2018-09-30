# GraphChart.py

from graphics import *

def initData(beg, year, apr):
	ret = [beg]
	for i in range(1, year+1):
		ret.append(round(ret[i-1]*(1+apr), 2))
	return ret

def main():
	win = GraphWin(title='Inverstment Growth Chart', width=320, height=240, autoflush=True)

	printlist = initData(2000, 10, 0.15)

	HEIGHT = 5

	leftbar = [str(i*2.5) + 'K' for i in range(HEIGHT)]

	for i in range(HEIGHT):
		label = Text(Point(20, 30+i*50), leftbar[-i-1])
		label.draw(win)

	for i in range(11):
		rect = Rectangle(Point(40+i*25, 230), Point(65+i*25, 230-printlist[i]*0.02))
		rect.setFill('green')
		rect.setWidth(2)
		rect.draw(win)

	win.mainloop()
	return 0

main()
