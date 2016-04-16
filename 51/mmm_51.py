import sys

def main():
	numList = processSTDIN()
	mean = getMean(numList)
	mode = getMode(numList)
	median = getMedian(numList)
	print("Mean: {:.1f}".format(mean))
	print("Mode: {:.1f}".format(mode))
	print("Median: {:.1f}".format(median))
	
def processSTDIN():
	numList = []
	for line in sys.stdin:
		numList.append(int(line.strip()))
	return numList

def getMedian(list):
	sortedList = sorted(list)
	
	length = len(sortedList)
	
	if length%2 == 0:
		lowerBound = length//2 - 1
		upperBound = length//2
		sum = sortedList[upperBound] + sortedList[lowerBound]
		return sum/2
		
	return sortedList[length//2]
	
#def getMode(list):
#	return max(set(list), key=list.count)

def getMode(list):
	
	dict = {}
	
	for num in list:
		try:
			dict[num] = dict[num] + 1
		except KeyError:
			dict[num] = 1
	
	highestNum = next(iter(dict.keys()))
	for key in dict.keys():
		if dict[highestNum] < dict[key]:
			highestNum = key
			
	return highestNum
	
	
def getMean(list):
	sum = 0
	for num in list:
		sum = sum + num
	return sum/len(list)
	
if __name__ == "__main__":
	main()