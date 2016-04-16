import sys

global maxIndex
global marks
global names
global maxStudents

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
		exit(0)
	
	global maxIndex
	maxIndex = 0
	
	global marks
	global names
	global maxStudents
	marks = list()
	names = list()
	maxStudents = list()
	
	processFile(f)
	
	sys.stdout.write("Best student(s):")
	for i in range(0, len(maxStudents)):
		sys.stdout.write(" " + maxStudents[i])
		if i < len(maxStudents)-1:
			sys.stdout.write(",")
	sys.stdout.write("\n")
	
	
	print("Best mark: " + str(marks[maxIndex]))

def getMark(wordvec):
	markString = wordvec[0]
	mark = 0
	try:
		mark = int(markString)
	except:
		print("Invalid mark " + markString + " encountered. Skipping.")
		return -1
		
	return mark
	
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
		if mark >= marks[maxIndex]:
			maxIndex = lineNumber
			global maxStudents
			maxStudents.append(name)
			
		lineNumber += 1
	

if __name__ == "__main__":
	main()