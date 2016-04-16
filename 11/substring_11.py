import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 3:
		exit(0)
		
	stringA = argv[1]
	stringB = argv[2]
	
	print(isSubstring(stringB, stringA))
	
def isSubstring(stringB, stringA):
	return stringB in stringA
	
if __name__ == "__main__":
	main()