import sys

def main():
	printHeaders()
	printRows()
	
def printRows():
	for line in sys.stdin:
		
		argv = line.split(" ")
		argc = len(argv)
		clubWords = argc-9
		
		pos = argv[0]
		club = ""
		for i in range(1, clubWords+1):
			if i>1:
				club = club + " "
			club = club + argv[i]
		
		p = argv[clubWords+1]
		w = argv[clubWords+2]
		d = argv[clubWords+3]
		l = argv[clubWords+4]
		gf = argv[clubWords+5]
		ga = argv[clubWords+6]
		gd = argv[clubWords+7]
		pts = argv[clubWords+8]
		
		sys.stdout.write('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>4s}'.format(pos, club, p, w, d, l, gf, ga, gd, pts))
		
def printHeaders():
	
	h1 = "POS"
	h2 = "CLUB"
	h3 = "P"
	h4 = "W"
	h5 = "D"
	h6 = "L"
	h7 = "GF"
	h8 = "GA"
	h9 = "GD"
	h10 = "PTS"
	
	print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))
	
if __name__ == "__main__":
	main()