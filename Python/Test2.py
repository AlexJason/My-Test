from sys import argv
from PIL import Image

def main(argc=0, argv=[]):
	im = Image.open(argv[1])
	im = im.convert('L')
	threshold = 200
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else :
			table.append(1)
	im = im.point(table, '1')
	im = im.convert('RGBA')
	data = im.getdata()
	newdata = list()
	for item in data:
		if item[0] > 220 and item[1] > 220 and item[2] > 220:
			newdata.append((255, 255, 255, 0))
		else:
			newdata.append(item)
	im.putdata(newdata)
	im.save(argv[1]+'bin.png', 'PNG')
	print('Picture saved:', argv[1], '->', argv[1]+'bin.png')
	return 0

if __name__ == '__main__':
	main(len(argv), argv)





