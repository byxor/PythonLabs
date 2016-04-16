import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
		
	fileName = argv[1]
	try:
		f = open(fileName)
	except:
		print("The file " + fileName + " could not be opened.")
		exit(0)
		
	studentData = processFile(f)

	printResults(studentData)

def printResults(studentData):
	
	highestIndices = getHighestIndices(studentData[0])
	
	#for i in highestIndices:
	#	print(i)
	#exit(0)
	
	names = []
	for i in range(0, len(highestIndices)):
		names.append(studentData[1][highestIndices[i]])
		
	sys.stdout.write("Best student(s):")
	for i in range(0, len(names)):
		sys.stdout.write(" " + names[i])
		if i < len(names)-1:
			sys.stdout.write(",")
	sys.stdout.write("\n")
	
	print("Best mark: " + str(studentData[0][highestIndices[0]]))
	
	
	
def processFile(f):
	
	studentData = []
	studentData.append([])
	studentData.append([])
	
	for line in f:
		wordv = line.split(" ")
		
		mark = getMark(wordv)
		if mark == "INVALID":
			continue
		name = getName(wordv)
		
		studentData[0].append(mark)
		studentData[1].append(name)
		
	return studentData
		
def getMark(wordv):
	markString = wordv[0]
	try:
		mark = int(markString)
	except:
		print("Invalid mark " + markString + " encountered. Skipping.")
		return "INVALID"
	return markString
	
def getName(wordv):
	name = ""
	for index in range(1, len(wordv)):
		if index>1:
			name += " "
		name += wordv[index]
	return name.strip()
	
def getHighestIndices(markVector):
	highestIndex = 0
	for index in range(0, len(markVector)):
		if int(markVector[index]) > int(markVector[highestIndex]):
			highestIndex = index
	
	highestMark = markVector[highestIndex]
	highestIndices = []
	for index in range(0, len(markVector)):
		if markVector[index] == highestMark:
			highestIndices.append(index)
			
	return highestIndices
	
	
if __name__ == "__main__":
	main()