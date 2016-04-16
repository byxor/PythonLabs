import sys

def main():
	frequencies = getFrequencies()
	printFrequencies(frequencies)

def printFrequencies(frequencies):
	for key, value in sorted(frequencies.items()):
		print("{} : {}".format(key, value))
	
def getFrequencies():
	frequencies = {}
	for line in sys.stdin:
		for word in line.split(" "):
			word = fix(word)
			if word in frequencies:
				frequencies[word] = frequencies[word] + 1
			else:
				frequencies[word] = 1
	return frequencies

def fix(word):
	word = word.lower()
	word = word.strip()
	word = word.replace(".", "")
	word = word.replace(",", "")
	word = word.replace("?", "")
	return word
	
if __name__ == "__main__":
	main()