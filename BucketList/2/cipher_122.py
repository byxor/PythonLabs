import sys
import operator

def main():
	init_alphabet()
	input = [line.strip() for line in sys.stdin]
	freq = calc_freq(input)
	max = calc_max(freq)
	shift = calc_shift(max)
	decoded = [decode(line, shift) for line in input]
	
	for line in decoded:
		print(line)

def init_alphabet():
	global alphabet
	alphabet = []
	alphabet.append('A')
	alphabet.append('B')
	alphabet.append('C')
	alphabet.append('D')
	alphabet.append('E')
	alphabet.append('F')
	alphabet.append('G')
	alphabet.append('H')
	alphabet.append('I')
	alphabet.append('J')
	alphabet.append('K')
	alphabet.append('L')
	alphabet.append('M')
	alphabet.append('N')
	alphabet.append('O')
	alphabet.append('P')
	alphabet.append('Q')
	alphabet.append('R')
	alphabet.append('S')
	alphabet.append('T')
	alphabet.append('U')
	alphabet.append('V')
	alphabet.append('W')
	alphabet.append('X')
	alphabet.append('Y')
	alphabet.append('Z')
	alphabet.append('0')
	alphabet.append('1')
	alphabet.append('2')
	alphabet.append('3')
	alphabet.append('4')
	alphabet.append('5')
	alphabet.append('6')
	alphabet.append('7')
	alphabet.append('8')
	alphabet.append('9')
		
def shift_char(ch, shift):
	global alphabet
	
	currentIndex=0
	for i in range(0, len(alphabet)):
		if ch == alphabet[i]:
			currentIndex = i
			break
	
	return alphabet[(currentIndex-shift) % len(alphabet)]
		
		
def decode(string, shift):
	decoded = ""
	for ch in string:
		isAlpha = ord(ch) in range(ord("A"), ord("Z")+1)
		isNum = ord(ch) in range(ord("0"), ord("9")+1)
		if isAlpha or isNum:
			decoded = decoded + shift_char(ch, shift)
		else:
			decoded = decoded + ch
	return decoded

def calc_shift(max):
	return ord(max) - ord("E")
	
def calc_freq(input):
	freq = {}
	
	for line in input:
		for word in line.split(" "):
			for ch in word.upper():
				if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
					try:
						freq[ch] = freq[ch]+1
					except KeyError:
						freq[ch] = 1
						
	return freq
	
def calc_max(freq):
	return max(freq.items(), key=operator.itemgetter(1))[0]

if __name__ == "__main__":
	main()