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

	#iterative version to find the longest sequence
	def longest_seq_iter(self, itemList):	
		LIS = []
		LIS.append([(1,0)])

		for i in range (1, len(itemList)):
			LIS.append([])
			for j in range (0, i):
				if( itemList[i][1] >= itemList[j][1]):
					if( len(LIS[i]) != 0 and ( LIS[i][0][0] < (LIS[j][0][0]+1))):
						del LIS[i][:]
					if( len(LIS[i]) == 0 or LIS[i][0][0] == (LIS[j][0][0]+1) ):
						num = LIS[j][0][0] + 1
						LIS[i].append( (num,j) )

				elif len(LIS[i]) == 0 :
					LIS[i].append((1,i))

  		self.printLIS(itemList, LIS)

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
	def find_last(self, current_last, previous):
		if current_last[1] > previous[1]:
			return current_last
		else:
			return previous


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




	#auxiliary function to obtain iterative cost




	def printLIS(self, lst, LIS):
		maxlen = 0
		for i in range (0, len(LIS)):
			if( LIS[i][0][0] > maxlen ):
				maxlen = LIS[i][0][0]

		for i in range (0, len(LIS)):
			if( LIS[i][0][0] == maxlen ):
				self.printLIS_h(lst, LIS, i, "")      

	def printLIS_h(self, lst, LIS, index, str):
		for tuple in range ( 0, len(LIS[index]) ):
			if( LIS[index][tuple][1] == index ):
				print lst[index],str
			else:
				self.printLIS_h(lst, LIS, LIS[index][tuple][1], `lst[index]`+" "+str)


	#to do
	# funcio per llegir de la entrada els elements



class Counter(object) :

    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self,*args, **kwargs) :
        self.counter += 1
        return self._fun(*args, **kwargs)

		

if __name__ == '__main__':

	seq = Sequence()
	step1 = seq.readFile('cargo.txt')
	#step2 = seq.longest_seq_rec(step1)
	step4 = seq.longest_seq_iter(step1)
	print step4


	#rec_lol = Counter(rec_lol)

#	factorial = Counter(factorial)
#	print factorial(int(sys.argv[1]))
#	print factorial.counter












