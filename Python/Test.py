from sys import argv

import os

def find(path, data=[]):
	file = os.listdir(path)
	for f in file:
		print(path+'\\'+f)
#		print(data)
		if os.path.isfile(path+'\\'+f):
			if f[-3:] == '.as':
				f = open(path+'\\'+f, encoding='utf-8', mode='r')
				d = 0
				n = 0
				for s in f:
					n += 1
					if -1 == s.find('//===========CLIP CC FUNCTION UPDATE BEG==========='):
						if -1 == s.find('//===========CLIP CC FUNCTION UPDATE END==========='):
							continue
						else:
							data.append([d, n])
					else:
						d = n
				f.close()
		else:
			data = find(path+'\\'+f, data)
	return data

def main(argc, argv):
	path = argv[1]
	data = find(path)
	sum0 = 0
	sum1 = len(data)
	for i in data:
		sum0 += i[1] - i[0] - 1

	print('Clip CC FUNCTION UPDATE源代码修处:')
	print('\t共修改: {} 处 {} 行'.format(sum1, sum0))
	
	return 0
	
if __name__ == '__main__':
	main(len(argv), argv)

