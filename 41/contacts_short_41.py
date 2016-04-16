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
		exit(0)

	contacts = getContacts(f)
	processInput(contacts)
	
	
def processInput(contacts):
	for line in sys.stdin:
		try:
			print("Phone: {}".format(contacts[line.strip("\n")]))
		except:
			print("No such contact")
	
def getContacts(f):
	contacts = {};
	for line in f:
		words = line.split(" ")
		name = words[0].strip("\n")
		number = words[1].strip("\n")
		#print(name + " " + number)
		contacts[name] = number
	return contacts

if __name__ == "__main__":
	main()