def init():
	global alphabet
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	global special
	special = ",. - '\n"


def shiftchar(c, amount):

	global alphabet
	if not c in alphabet:
		return c

	cur_index = alphabet.index(c)
	new_index = (cur_index+amount) % len(alphabet)

	return alphabet[new_index]


def shift_string(s, amount):
	shifted = ""
	for c in s:
		shifted += shiftchar(c, amount)
	return shifted


def get_difference(a, b):
	global alphabet
	return alphabet.index(b) - alphabet.index(a)


def get_dicto(s):
	global alphabet
	dicto = {}
	for c in s:
		if not c in alphabet:
			continue
		try:
			dicto[c] += 1
		except KeyError:
			dicto[c] = 1
	return dicto


def main():
	import sys
	import operator
	init()
	stdin = "".join([line for line in sys.stdin])
	dicto = get_dicto(stdin)
	echar = max(dicto.items(), key=operator.itemgetter(1))[0]
	amount = get_difference(echar, "E")
	deciphered = shift_string(stdin, amount)
	sys.stdout.write(deciphered)


if __name__ == "__main__":
	main()
