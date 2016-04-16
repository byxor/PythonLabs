import math
import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
		
	dec=0
	try:
		dec = int(argv[1])
	except:
		exit(0)

	print("{:.{}f}".format(math.pi, dec))
	
if __name__ == "__main__":
	main()