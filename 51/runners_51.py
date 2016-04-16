import sys

def main():
	data_list = process_std_in()
	runner_list = process_data(data_list)
	fastest = get_fastest(runner_list)
	print("{} : {}".format(fastest[0], fastest[1]))
	
def get_fastest(runner_list):
	
	fastest = runner_list[0]
	for i in range(1, len(runner_list)):
		if decode_time(runner_list[i][1]) < decode_time(fastest[1]):
			fastest = runner_list[i]
	
	return fastest

def process_data(data_list):
	runner_list = []
	for data in data_list:
		
		valid_runner = True
		data_split = data.split(" ")
		
		times = []
		for i in range(1, len(data_split)):
			time_string = data_split[i]
			
			try:
				time = decode_time(time_string)
			except ValueError:
				valid_runner = False
			
			times.append(time)
		
		name = data_split[0]
		best_time = min(times)
		
		runner = (name, encode_time(best_time))
		
		if valid_runner == True:
			runner_list.append(runner)
	
	return runner_list
	
def process_std_in():
	data = []
	for line in sys.stdin:
		data.append(line.strip())
	return data
	
def encode_time(time_int):
	minutes = time_int//60
	seconds = time_int%60
	return "{}:{:02d}".format(minutes, seconds)

def decode_time(time_string):
	time_split = time_string.split(":")
	minutes = int(time_split[0])
	seconds = int(time_split[1])
	return minutes*60 + seconds
	
if __name__ == "__main__":
	main()