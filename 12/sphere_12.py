import math
import sys

def main():
	
	argv = sys.argv
	argc = len(argv)
	
	if argc < 4:
		exit(0)
		
	startRadius=0.0
	step=0.0
	endRadius=0.0
	
	try:
		startRadius = float(argv[1])
		step = float(argv[2])
		endRadius = float(argv[3])
	except:
		exit(0)
		
	printTable(startRadius, step, endRadius)
	
def calcArea(r):
	return 4*math.pi*r*r
	
def calcVolume(r):
	r3 = r*r*r
	coeff = 4/3
	return coeff*math.pi*r3

def printRows(startRadius, step, endRadius):
	
	r = startRadius
	while r <= endRadius:
	
		a = calcArea(r)
		v = calcVolume(r)
		
		rString = "{0: >10}".format("{:.1f}".format(r))
		aString = "{0: >10}".format("{:.2f}".format(a))
		vString = "{0: >12}".format("{:.2f}".format(v))
		
		print("{}      {}    {}".format(rString, aString, vString))
		
		r += step

def printHeadings():
	print("Radius (m)      Area (m^2)    Volume (m^3)")
	print("----------      ----------    ------------")
	
def printTable(startRadius, step, endRadius):
	printHeadings()
	printRows(startRadius, step, endRadius)
	
if __name__ == "__main__":
	main()