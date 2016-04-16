import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
	
	inputString = argv[1]
	
	if len(inputString) == 0:
		exit(0)
		
	print(getMiddle(inputString))

def getMiddle(string):
	
	length = len(string)
	
	if length % 2 == 0:
		return "No middle character!"
		
	midIndex = int(length/2)
	return string[midIndex]
		
if __name__ == "__main__":
	main()