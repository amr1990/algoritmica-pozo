import sys

class Sequence(object):


	#function to read the file and return a list of elements
	def readFile(self, file):
		f = open(file, "r")
		itemList = []
		for line in f.readlines():
			parsed_line = line.split();
			itemList.append((parsed_line[0],int(parsed_line[1])))

		return itemList

	def readFromInput(self):
		itemList = []
		print "Introdueix parelles producte altura. Per finalitzar prem Control+D"
		inp = sys.stdin.readlines()
		for line in inp:
		    parse = line.split()
		    itemList.append((parse[0], int(parse[1])))

		print "------------------------------------------------------------------"
		return itemList

	#iterative version to find the longest sequence
	def longest_seq_iter(self, itemList):
		n = len(itemList)
		dp = [(0, -1)]*n
			# dp contains (best, idx) tuples, where best is the length of the longest
			# increasing sequence starting from that element, and idx is the index of the
			# longest increasing sequence
		for i in range(n-1, -1, -1):
			best = 0
			idx = -1
			for j in range(i+1, n):
				if itemList[i][1] < itemList[j][1] and dp[j][0] + 1 > best:
					best = dp[j][0] + 1
					idx = j
			dp[i] = (best, idx)

		longest = self.get_longest_seq(itemList, dp)

		return longest

	#recursive version to find the longest sequence
	def longest_seq_rec(self, itemList, last_increase=0):
		if len(itemList) == 0:
			return itemList

		longest = self.longest_seq_rec(itemList[1:], last_increase)
		current = itemList[0]

		if (current[1] > last_increase):
			currentList = [current] + self.longest_seq_rec(itemList[1:], current[1])

			longest = self.get_longest_list(currentList, longest)

		return longest


	#auxiliary function to find the last increasing element
	def get_longest_seq(self, itemList, indexList):
		result = []

		idx = max(range(len(itemList)), key=lambda i: indexList[i][0])

		while idx != -1:
			result.append(itemList[idx])
			_, idx = indexList[idx]
		return result

	#auxiliary function to obtain the longest size list
	def get_longest_list(self, list1, list2):
		if len(list1) > len(list2):
			return list1
		else:
			return list2


	#auxiliary function to make the result format match the test
	def patch_out(self, itemList):
		for elem in itemList:
			print elem[0], elem[1]


	#auxiliary function to obtain iterative cost
	def get_cost_iter(self, itemList, cost=0):
		n = len(itemList)
		dp = [(0, -1)]*n
		for i in range(n-1, -1, -1):
			best = 0
			idx = -1
			cost = cost + 1
			for j in range(i+1, n):
				if itemList[i][1] < itemList[j][1] and dp[j][0] + 1 > best:
					best = dp[j][0] + 1
					idx = j
					cost = cost +1
			dp[i] = (best, idx)

		longest = self.get_longest_seq(itemList, dp)
		return cost


	#auxiliary function to obtain iterative cost
	def get_cost_rec(self, itemList):
		self.longest_seq_rec = Counter(self.longest_seq_rec)
		test = self.longest_seq_rec(itemList)

		return self.longest_seq_rec.counter




class Counter(object) :

    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self,*args, **kwargs) :
        self.counter += 1
        return self._fun(*args, **kwargs)



if __name__ == '__main__':
	seq = Sequence()
	if len(sys.argv) == 1:
		step1 = seq.readFromInput()

		#step2a = seq.longest_seq_iter(step1)
		#step2b = seq.patch_out(step2a)

		step3a = seq.longest_seq_rec(step1a)
		step3b = seq.patch_out(step3a)
		#step3c = seq.get_cost_rec(step1a)
		#print 'cost: ',step3c
	else:
		step1 = seq.readFile(sys.argv[1])

		#step2a = seq.longest_seq_iter(step1)
		#step2b = seq.patch_out(step2a)

		step3a = seq.longest_seq_rec(step1)
		step3b = seq.patch_out(step3a)
		#step3c = seq.get_cost_rec(step1)
		#print 'cost: ',step3c
