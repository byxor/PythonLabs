import sys
import operator

def main():
	frequencies = getFrequencies()
	printFrequencies(frequencies)

def printFrequencies(frequencies):
	for key, value in sorted(frequencies.items(), key=operator.itemgetter(1))[::-1]:
		print("{} : {:>3}".format(key, value))

def getFrequencies():
	frequencies = {}
	frequencies["a"] = 0
	frequencies["e"] = 0
	frequencies["i"] = 0
	frequencies["o"] = 0
	frequencies["u"] = 0
	
	for line in sys.stdin:
		for word in line.split(" "):
			word = fix(word)
			for char in word:
				try:
					frequencies[char] = frequencies[char] + 1
				except:
					pass
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