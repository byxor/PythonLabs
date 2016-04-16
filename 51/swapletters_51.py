import sys

def main():
	
	argv = sys.argv
	argc = len(argv)
	if argc < 2:
		exit(0)
		
	word = argv[1]
	swapped = swap(word)
	
	print(swapped)
	
def swap(word):
	
	length = len(word)
	halfLength = int(length/2)
	
	swapped = ""
	for i in range(0, halfLength):
		swapped = swapped + word[i*2+1] + word[i*2]
		
	if length%2!=0:
		swapped = swapped + word[length-1]
		
	return swapped

if __name__ == "__main__":
	main()