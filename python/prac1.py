import sys

def readFile(f):

	f = open(f, "r")
	itemList = []
	for line in f.readlines():
		parsed_line = line.split();
		itemList.append((parsed_line[0],parsed_line[1]))

	return itemList


def trol_sort_it(li):	
	cur_max_h = 0
	cur_max_l = []
	max_l = []
	
	for tup in li:
		#each element
		cur_max_l = find_max(li[li.index(tup):])
		if len(cur_max_l) > len(max_l):
			max_l = cur_max_l

	return max_l


def find_max(li):
	max_l = []
	last = 0
	for line in li:
		if line[1] > last:
			max_l.append(line)
			last = line[1]
	return max_l


def trol_sort_rec(li):
	#to do
	if len(li) == 1:
		return li
	else:
		ms = find_max(li)
		return max(ms, trol_sort_rec(li[1:]))


if __name__ == '__main__':

	p = readFile(sys.argv[1])
	print trol_sort_it(p)