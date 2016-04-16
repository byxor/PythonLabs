import sys

def main():
	
	stdinList = readStandardInput()
	
	length17 = ["'"+word+"'" for word in stdinList if len(word)==17]
	printList("Words containing 17 letters: ", length17)
	
	length18plus = ["'"+word+"'" for word in stdinList if len(word)>=18]
	printList("Words containing 18+ letters: ", length18plus)
	
	vowelList = ["'"+word+"'" for word in stdinList if hasAllVowels(word)]
	indexOfShortest = 0
	for i in range(1, len(vowelList)):
		if len(vowelList[i]) < len(vowelList[indexOfShortest]):
			indexOfShortest = i
	print("Shortest word containing all vowels: " + vowelList[indexOfShortest].replace("'", ""))
	
	fourAList = ["'"+word+"'" for word in stdinList if hasNChars(4, "a", word)]
	printList("Words with 4 a's: ", fourAList)
	
	twoPlusQList = ["'"+word+"'" for word in stdinList if hasNPlusChars(2, "q", word)]
	printList("Words with 2+ q's: ", twoPlusQList)
	
	containsCieList = ["'"+word+"'" for word in stdinList if ("cie" in word)]
	printList("Words containing cie: ", containsCieList)
	
	anagramAngleList = ["'"+word+"'" for word in stdinList if isAnagram(word, "angle")]
	printList("Anagrams of angle: ", anagramAngleList)
	
	endsWithIaryList = ["'"+word+"'" for word in stdinList if word.endswith("iary")]
	print("Words ending in iary: " +  str(len(endsWithIaryList)))
	
	qMedInteUList = ["'"+word+"'" for word in stdinList if containsQMedInteU(word)]
	for i in range(0, len(qMedInteUList)):
		if qMedInteUList[i]=="'q's'":
			qMedInteUList[i] = "\"q's\""
	printList("Words with q but no u: ", qMedInteUList)
	
	mostEList = getMostEs(stdinList)
	printList("Words with most e's: ", mostEList)
	
def getMostEs(list):
	maxE = 0
	for i in range(0, len(list)):
		e = getCharCount("e", list[i])
		if maxE < e:
			maxE = e
	return ["'"+word+"'" for word in list if getCharCount("e", word)==maxE]

def getCharCount(char, string):
	count = 0
	for c in string:
		if c.lower() == char.lower():
			count += 1
	return count

	
def containsQMedInteU(string):
	length = len(string)
	for i in range(0, length-1):
		if ((string[i].lower()=="q") and (string[i+1].lower()!="u")):
			return True
	return string[length-1].lower()=="q"
	
def isAnagram(stringA, stringB):
	
	stringA = stringA.lower()
	stringB = stringB.lower()
	
	if stringA == stringB:
		return False
	
	lengthA = len(stringA)
	lengthB = len(stringB)
	if lengthA != lengthB:
		return False
	
	for indexA in range(0, lengthA):
		charA = stringA[indexA]
		
		lengthB = len(stringB)
		for indexB in range(0, lengthB):
			charB = stringB[indexB]
		
			if charA == charB:
				stringB = stringB.replace(charB, "", 1)
				break
				
			if indexB == lengthB-1:
				return False
				
	return True
	
def hasAllVowels(string):
	string = string.lower()
	return ("a" in string) and ("e" in string) and ("i" in string) and ("o" in string) and ("u" in string)
	
def hasNChars(number, character, string):
	occurences = 0
	string = string.lower()
	for char in string:
		if char == character:
			occurences += 1
	return (occurences==number)

def hasNPlusChars(number, character, string):
	occurences = 0
	string = string.lower()
	for char in string:
		if char == character:
			occurences += 1
	return (occurences>=number)
	
def readStandardInput():
	stdinList = list()
	for line in sys.stdin:
		stdinList.append(line.strip())
	return stdinList
	
def printList(suffix, list):
	length = len(list)
	sys.stdout.write(suffix)
	sys.stdout.write("[")
	for i in range(0, length):
		sys.stdout.write(str(list[i]))
		if i < length-1:
			sys.stdout.write(", ")
	sys.stdout.write("]\n")

if __name__ == "__main__":
	main()