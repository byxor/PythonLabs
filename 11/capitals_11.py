import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
		
	inputString = argv[1]
		
	if len(inputString) < 2:
		exit(0)

	print(capitalise(inputString))
	
def capitalise(string):
	
	return string[0].upper() + string[1:len(string)-1] + string[len(string)-1].upper()
		
if __name__ == "__main__":
	main()