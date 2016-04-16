import sys

def main():
	words = processSTDIN()
	evilWords = [word for word in words if isEvil(word)]
	for evilWord in evilWords:
		print(evilWord)
	
def processSTDIN():
	words = []
	for line in sys.stdin:
		words.append(line.strip())
	return words
	
def isEvil(word):
	evil = ["e", "v", "i", "l"]
	currentIndex = 0
	for character in word:
		if currentIndex == 4:
			break
		if character.lower() == evil[currentIndex]:
			currentIndex = currentIndex + 1
			
	if currentIndex < 4:
		return False
		
	letterCount = {}
	letterCount["e"] = countLetter("e", word)
	letterCount["v"] = countLetter("v", word)
	letterCount["i"] = countLetter("i", word)
	letterCount["l"] = countLetter("l", word)
	for item in letterCount.items():
		if item[1] > 1:
			return False
			
	return True
	
def countLetter(letter, word):
	count = 0
	for char in word:
		if char.lower() == letter:
			count = count + 1
	return count


if __name__ == "__main__":
	main()