import sys

def main():

	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)

	noun = argv[1]
	
	if len(noun) == 0:
		exit(0)
		
	print(getPlural(noun))
	
def getPlural(noun):
	c = noun[len(noun)-2]
	if noun.endswith("ch") or noun.endswith("sh") or noun.endswith("x") or noun.endswith("s") or noun.endswith("z"):
		return noun + "es"
	elif noun.endswith("o"):
		return noun + "es"
	elif noun.endswith("f"):
		return noun[0:len(noun)-1] + "ves"
	elif noun.endswith("fe"):
		return noun[0:len(noun)-2] + "ves"
	elif noun.endswith("y") and c!='a' and c!="e" and c!="i" and c!="o" and c!="u":
		return noun[0:len(noun)-1] + "ies"	
	else:
		return noun + "s"
		
if __name__ == "__main__":
	main()