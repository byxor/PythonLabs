import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
		
	inputString = argv[1]
	
	if len(inputString) <= 2:
		exit(0)

	print(chop(inputString))
		
def chop(string):
	return string[1:len(string)-1]

if __name__ == "__main__":
	main()