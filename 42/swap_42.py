def swap_keys_values(dictionary):	
	swapped = {}
	for item in dictionary.items():
		swapped[item[1]] = item[0]
	return swapped