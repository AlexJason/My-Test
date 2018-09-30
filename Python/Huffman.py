import sys
import copy

class HuffmanTree():
	def __init__(self):
		self.left = HuffmanNode(True)
		self.right = HuffmanNode(False)

class HuffmanNode():
	def __init__(self, char=b'', value=0, bottom=False, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.bottom = bottom
		self.char = char

def Create_CharDict(string, time_list=list(), char_list=list()):
	for c in string:
		if c not in char_list:
			char_list.append(c)
			time_list.append(0)
		time_list[char_list.index(c)] += 1
	return (time_list, char_list)

def Create_HuffmanDict(time_list, char_list):
	def Search(node, code=''):
		if not node.bottom:
			Search(node.left, code=code+'0')
			Search(node.right, code=code+'1')
		else:
			huffman_dict[node.char] = code
	
	forest = [HuffmanNode(value=time_list[i], char=char_list[i], bottom=True) for i in range(len(time_list))]
	
	while len(forest) > 1:
		value_list = [x.value for x in forest]
		tmp = copy.copy(value_list)
		tmp.sort()
		i = value_list.index(tmp[0])
		value_list[i] = -1
		j = value_list.index(tmp[1])
		node = HuffmanNode(left=forest[i], right=forest[j], value=(forest[i].value+forest[j].value))
		forest.pop(i)
		forest.pop(j-1 if j>i else j)
		forest.insert(i, node)
	huffman_dict = dict()
	Search(forest[0])
	return huffman_dict

def String_HuffmanDict(huffman_dict):
	compressed_string = bytes()
	for k in huffman_dict:
		compressed_string += bytes(chr(k), encoding='utf-8')
		compressed_string += bytes(chr(len(huffman_dict[k])), encoding='utf-8')
		tmp = bytes(chr(int(huffman_dict[k], 2)), encoding='utf-8')
		if len(tmp) == 1:
			tmp = b'\x00' + tmp
		compressed_string += tmp
	table_len = bytes(chr(len(compressed_string)), encoding='utf-8')
	if len(table_len) == 1:
		table_len = b'\x00' + table_len
	compressed_string = table_len + compressed_string
	return compressed_string

def Compresse_Huffman(string, huffman_dict):
	compressed_string = bytes()
	text = ''
	for s in string:
		text += huffman_dict[s]
	if len(text) % 7 != 0:
		text += '0'*(len(text) % 7)
	for i in range(0, len(text), 7):
		compressed_string += bytes(chr(int(text[i:][:7], 2)), encoding='utf-8')
	return compressed_string

def main():
	#name = 'ClipCC Main.exe'
	#name = 'FL Studio VSTi.dll'
	#name = 't1.txt'
	#name = 'Test_Huffman_1_in.txt'
	name = sys.argv[1]
	prt = bool(int(sys.argv[2]))

	path = './cache/'+name
	ifile = open(path, 'rb')
	size = 1024*20

	time_list = list()
	char_list = list()
	file_str = ifile.read(size)
	times = 0
	while len(file_str) != 0:
		time_list, char_list = Create_CharDict(file_str, time_list, char_list)
		file_str = ifile.read(size)
		huffman_dict = Create_HuffmanDict(time_list, char_list)
		times += size
		if prt:
			print(times)
	ifile.close()

	huffman_dict = Create_HuffmanDict(time_list, char_list)
	ofile = open(path+'.huf.filter', 'wb')
	ofile.write(String_HuffmanDict(huffman_dict))
	ofile.close()

	ifile = open(path, 'rb')
	ofile = open(path+'.huf', 'wb')
	ofile.close()
	file_str = ifile.read(size)
	times = 0
	while len(file_str) != 0:
		ofile = open(path+'.huf', 'ab')
		ofile.write(Compresse_Huffman(file_str, huffman_dict))
		ofile.close()
		file_str = ifile.read(size)
		times += size
		if prt:
			print(times)
	ifile.close()


if __name__ == '__main__':
	main()
