import sys

def main():
	for line in sys.stdin:
		
		input = [int(num) for num in line.split()]
		
		a=input[0]
		b=input[1]
		c=input[2]
		
		discriminant = getDiscriminant(a, b, c)
		if discriminant < 0:
			print ("None")
			continue
		
		roots = []
		roots.append(((-b)+((discriminant)**0.5))/(2*a))
		roots.append(((-b)-((discriminant)**0.5))/(2*a))
		
		print ("r1 = {}, r2 = {}".format(roots[0], roots[1]))
			
def getDiscriminant(a, b, c):
	return (b**2) - (4*a*c)
	
if __name__ == "__main__":
	main()