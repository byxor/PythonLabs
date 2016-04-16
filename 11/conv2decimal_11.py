import sys
import math

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 3:
		exit(0)
	
	numberString = argv[1]
	baseString = argv[2]
	
	base=0
	try:
		base = int(baseString)
	except:
		exit(0)

	print(convertToDecimal(numberString, base))
	
def convertToDecimal(numberString, base):
	length = len(numberString)
	value = 0
	for index in range(0, length):
		value += int(numberString[index]) * pow(base, length-index-1)
	return value
	
if __name__ == "__main__":
	main()