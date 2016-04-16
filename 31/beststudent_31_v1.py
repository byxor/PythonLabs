import sys

global maxIndex
global marks
global names

def main():
	
	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(1)
		
	fileName = argv[1]
		
	try:
		f = open(fileName)
	except:
		print("The file " + fileName + " could not be opened.")
		exit(1)
	
	global maxIndex
	maxIndex = 0
	
	global marks
	marks = list()
	
	global names
	names = list()
	
	processFile(f)
	
	print("Best student: " + names[maxIndex])
	print("Best mark: " + str(marks[maxIndex]))

def getMark(wordvec):
	return int(wordvec[0])
	
def getName(wordvec):
	name = ""
	for i in range(1, len(wordvec)):
		if i > 1:
			name += " "
		name += wordvec[i]
	return name.strip()
	
def processFile(f):
	lineNumber = 0
	for line in f:
		
		wordvec = line.split(" ")
		
		mark = getMark(wordvec)
		global marks
		marks.append(mark)
		
		name = getName(wordvec)
		global names
		names.append(name)
		
		global maxIndex
		if mark > marks[maxIndex]:
			maxIndex = lineNumber
			
		lineNumber += 1
	

if __name__ == "__main__":
	main()