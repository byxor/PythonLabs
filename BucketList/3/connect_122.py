import sys

def get_verticals(grid):
	H = len(grid[0])
	V = len(grid)
	verticals = []
	for x in range(0, H):
		string = ""
		for y in range(0, V):
			string = string + grid[y][x]
		verticals.append(string)
	return verticals

def get_diagonals_f(grid):
	H = len(grid[0])
	V = len(grid)
	diagonals_f = []
	
	#slide along side
	for rooty in range(V-1,-1,-1):
		string = ""
		x = 0
		y=rooty
		string = ""
		while x<H and x>=0 and y<V and y>=0:
			string = string + grid[y][x]
			x = x + 1
			y = y + 1
		diagonals_f.append(string)
	
	#slide across top
	for rootx in range(1, H):
		string = ""
		x = rootx
		y = 0
		while x<H and x>=0 and y<V and y>=0:
			string = string + grid[y][x]
			x = x + 1
			y = y + 1
		diagonals_f.append(string)
	
	return diagonals_f
	
def get_diagonals_b(grid):
	H = len(grid[0])
	V = len(grid)
	diagonals_b = []
	
	#slide along side
	for rooty in range(V-1,-1,-1):
		string = ""
		x = H-1
		y=rooty
		string = ""
		while x<H and x>=0 and y<V and y>=0:
			string = string + grid[y][x]
			x = x - 1
			y = y + 1
		diagonals_b.append(string)
	
	#slide across top
	for rootx in range(H-2, -1, -1):
		string = ""
		x = rootx
		y = 0
		while x<H and x>=0 and y<V and y>=0:
			string = string + grid[y][x]
			x = x - 1
			y = y + 1
		diagonals_b.append(string)
	
	return diagonals_b
	
	
def count_matches(pattern, lines):
	matches = 0
	for line in lines:
		if pattern in line:
			matches = matches + 1
	return matches

def get_pcount(grid, ln):

	horizontals = grid
	verticals = get_verticals(grid)
	diagonals_f = get_diagonals_f(grid)
	diagonals_b = get_diagonals_b(grid)

	#print("horizontals:")
	#print(horizontals)
	#print()
	#print("verticals:")
	#print(verticals)
	#print()
	#print("diagonals_f")
	#print(diagonals_f)
	#print()
	#print("diagonals_b")
	#print(diagonals_b)
	
	pattern = ""
	for i in range(0, ln):
		pattern = pattern + "x"

	pcount = 0
	pcount = pcount + count_matches(pattern, horizontals)
	pcount = pcount + count_matches(pattern, verticals)
	pcount = pcount + count_matches(pattern, diagonals_f)
	pcount = pcount + count_matches(pattern, diagonals_b)

	return pcount
	
def main():
	
	argv = sys.argv
	argc = len(argv)
	
	if argc < 2:
		exit(0)
	
	grid = [line.strip() for line in sys.stdin]
	ln = int(argv[1])
	
	print(get_pcount(grid, ln))

if __name__ == "__main__":
	main()