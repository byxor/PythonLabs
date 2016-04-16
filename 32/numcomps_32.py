import sys
import copy

def main():

	numList = generateList(30)
	
	multiples3 = [n for n in numList if n%3==0]
	printList("Multiples of 3: ", multiples3)
	
	multiples3pow2 = [n**2 for n in numList if n%3==0]
	printList("Multiples of 3 squared: ", multiples3pow2)
	
	multiples4x2 = [n*2 for n in numList if n%4==0]
	printList("Multiples of 4 doubled: ", multiples4x2)
	
	multiples3or4 = [n for n in numList if (n%3==0 or n%4==0)]
	printList("Multiples of 3 or 4: ", multiples3or4)
	
	multiples3and4 = [n for n in numList if (n%3==0 and n%4==0)]
	printList("Multiples of 3 and 4: ", multiples3and4)
	
	multiples3medx = generateList(30)
	for i in range(0, len(multiples3medx)):
		if multiples3medx[i]%3==0:
			multiples3medx[i] = "'X'"
	printList("Multiples of 3 replaced: ", multiples3medx)
	
def printList(suffix, list):
	
	length = len(list)
	
	sys.stdout.write(suffix)
	sys.stdout.write("[")
	
	for i in range(0, length):
		
		sys.stdout.write(str(list[i]))
		
		if i < length-1:
			sys.stdout.write(", ")
			
	sys.stdout.write("]\n")
	

def generateList(number):
	numberList = list()
	for i in range(1, number+1):
		numberList.append(i)
	return numberList

if __name__ == "__main__":
	main()