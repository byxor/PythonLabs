import sys

def main():
	
	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
		
	password = argv[1]
	
	print(get_num_of_char_classes(password))
	
def get_num_of_char_classes(password):
	
	length = len(password)
	
	if length == 0:
		return 0
		
	char_class = [0, 0, 0, 0]
	#hasDigit, hasLower, hasUpper, hasSpecial
		
	for c in password:
		value = ord(c)
		if value>=ord("0") and value<=ord("9"):
			char_class[0] = 1
		elif value>=ord("a") and value<=ord("z"):
			char_class[1] = 1
		elif value>=ord("A") and value<=ord("Z"):
			char_class[2] = 1
		else:
			char_class[3] = 1
	
	return calc_sum(char_class)
		
def calc_sum(list):
	sum = 0
	for num in list:
		sum += num
	return sum
		
if __name__ == "__main__":
	main()