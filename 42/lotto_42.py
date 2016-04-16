import sys
import random

def main():

	argv = sys.argv
	argc = len(argv)
	if argc < 7:
		exit(1)
	
	winningNumbers = []
	for i in range(1, 7):
		winningNumbers.append(int(argv[i]))
		
	matchesDict = createMatchesDict()
	
	runs = 1000000
	
	random.seed()
	for i in range(0, runs):
		print(i)
		randomNumbers = generateNumbers(6)
		matches = getMatches(randomNumbers, winningNumbers)
		if matches in matchesDict:
			matchesDict[matches] = matchesDict[matches] + 1
	
	printResults(matchesDict, runs)
	
def printResults(matchesDict, runs):
	for i in range(3, 7):
		matches = matchesDict[i]
		
		try:
			probability = round(runs/matches)
		except:
			probability = "?"
		
		sys.stdout.write("Match {}'s : {:>5} ({} to 1)\n".format(i, matches, probability))
	
def generateNumbers(length):
	randomNumbers = []
	for i in range(0, length):
		randomNumbers.append(random.randint(1, 47))
	return randomNumbers

def getMatches(yourNumbers, winningNumbers):
	
	matches = 0
	
	yourLength = len(yourNumbers)
	for yourIndex in range(0, yourLength):
		yourNumber = yourNumbers[yourIndex]
		
		winningLength = len(winningNumbers)
		for winningIndex in range(0, winningLength):
			winningNumber = winningNumbers[winningIndex]
			
			if yourNumber == winningNumber:
				matches = matches + 1
				winningNumbers.remove(winningNumber)
				break
				
	return matches
	
def createMatchesDict():
	matchesDict = {}
	for i in range(3, 7):
		matchesDict[i] = 0
	return matchesDict
	
if __name__ == "__main__":
	main()