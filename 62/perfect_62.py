import sys

def main():
	nums = [int(line.strip()) for line in sys.stdin]
	for n in nums:
		print(isPerfect(n))

def sumFac(n):
	if n <= 1:
		return 0
	sum = 1
	#print(n)
	for i in range(2, n//2+1):
		if n%i==0:
			#print("{:>4}".format(i))
			sum = sum + i
	return sum
	
def isPerfect(n):
	return n == sumFac(n)
	
if __name__ == "__main__":
	main()