def swap_unique_keys_values(dictionary):
	unique_swapped = {}
	for item in dictionary.items():
		if getOccurences(item[1], dictionary.values()) < 2:
			unique_swapped[item[1]] = item[0]
	return unique_swapped
	
def getOccurences(yourThing, collection):
	occurences = 0
	for object in collection:
		if object == yourThing:
			occurences = occurences + 1
	return occurences