# GraphConvert.py

from graphics import *

def fahrenheit(celsius):
	return 9.0 / 5.0 * celsius + 32

def main():
	win = GraphWin('Celsius Converter', 400, 300)
	win.setCoords(0, 0, 3, 4)

	Text(Point(1,3), 'Celsius Temperature:').draw(win)
	Text(Point(1,1), 'Fahrenheit Temperature:').draw(win)

	inputText = Entry(Point(2.25, 3), 5)
	inputText.setText('0.0')
	inputText.draw(win)

	outputText = Text(Point(2.25, 1), '')
	outputText.draw(win)

	button = Text(Point(1.5, 2.0), 'Convert It')
	button.draw(win)

	Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

	win.getMouse()

	celsius = float(inputText.getText())
	outputText.setText(round(fahrenheit(float(inputText.getText())), 2))
	button.setText('Quit')

	win.getMouse()
	win.close()
	return 0

main()
