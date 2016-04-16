import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
	
	size = 0
	try:
		size = int(argv[1])
	except:
		exit(0)
	
	drawDiamond(size)

def drawDiamond(size):
	for i in range(0, size):
		for j in range(0, size-i-1):
			sys.stdout.write(" ")
		for j in range(0, i+1):
			sys.stdout.write("* ")
		print()

	for i in range(size-2, -1, -1):
		for j in range(0, size-i-1):
			sys.stdout.write(" ")
		for j in range(0, i+1):
			sys.stdout.write("* ")
		print()
		
if __name__ == "__main__":
	main()