import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	rankCounts = getRankCounts()
	totalHands = getTotalHands(rankCounts)

	rankStrings = getRankStrings()
	results = getResults(rankCounts, totalHands)
	
	printResults(rankStrings, results)
	
def getResults(rankCounts, totalHands):
	
	results = []
	
	for i in range(0, len(rankCounts)):
		results.append(rankCounts[i]/totalHands)
	
	return results
	
def printResults(rankStrings, results):
	
	for i in range(0, len(results)):
		sys.stdout.write("The probability of ")
		sys.stdout.write(rankStrings[i])
		sys.stdout.write(" is ")
		sys.stdout.write("{:.4f}".format(results[i]*100))
		sys.stdout.write("%\n")
	
def getTotalHands(rankCounts):
	sum = 0
	for i in range(0, len(rankCounts)):
		sum += rankCounts[i]
	return sum
	
def getRankStrings():

	rankStrings = []
	
	rankStrings.append("nothing")
	rankStrings.append("one pair")
	rankStrings.append("two pairs")
	rankStrings.append("three of a kind")
	rankStrings.append("a straight")
	rankStrings.append("a flush")
	rankStrings.append("a full house")
	rankStrings.append("four of a kind")
	rankStrings.append("a straight flush")
	rankStrings.append("a royal flush")
	
	return rankStrings

def getRankCounts():
	
	rankCounts = []
	
	for i in range(0, 10):
		rankCounts.append(0)
	
	for line in sys.stdin:
		rank = getRank(line)
		rankCounts[rank] += 1
		
	return rankCounts

def getRank(line):
	splitLine = line.split(",")
	rankString = splitLine[len(splitLine)-1]
	rank = int(rankString)
	return rank
	
if __name__ == "__main__":
	main()