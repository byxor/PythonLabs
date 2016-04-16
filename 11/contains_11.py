import sys

def main():
	
	argv = sys.argv
	argc = len(argv)
	
	if argc < 3:
		exit(0)
		
	stringA = argv[1]
	stringB = argv[2]
		
	print(contains(stringA, stringB))
	
def contains(stringA, stringB):
	
	lengthA = len(stringA)
	for indexA in range(0, lengthA):
		
		charA = stringA[indexA]
		
		lengthB = len(stringB)
		for indexB in range(0, lengthB):
			charB = stringB[indexB]
			#print("comparing " + charA + " to " + charB)
			if charA == charB:
				stringB = stringB.replace(charB, "", 1)
				break
			if indexB == lengthB-1:
				return False
				
	return True




if __name__ == "__main__":
	main()