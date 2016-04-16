import sys
import re

def main():
	text = process_stdin()
	
	reg_dates_slashes = re.compile("[\d]{1,2}\/[\d]{1,2}\/[\d]{1,2}")
	list_dates_slashes = reg_dates_slashes.findall(text)
	print(list_dates_slashes)
	
	reg_dates_hyphens = re.compile("[\d]{1,2}-[\d]{1,2}-[\d]{1,2}")
	list_dates_hyphens = reg_dates_hyphens.findall(text)
	print(list_dates_hyphens)
	
	reg_dates_both = re.compile("[\d]{1,2}[\/-][\d]{1,2}[\/-][\d]{1,2}")
	list_dates_both = reg_dates_both.findall(text)
	print(list_dates_both)
	
	reg_phones = re.compile("01[- ][\d]{7}")
	list_phones = reg_phones.findall(text)
	print(list_phones)
	
	reg_emails = re.compile("(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*")
	list_emails = reg_emails.findall(text)
	print(list_emails)
	
	reg_dates_words = re.compile("([\d]{1,2})( )(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Nov|Dec)( )([\d]{2,4})")
	list_dates_words = reg_dates_words.findall(text)
	list_dates_words_fixed = ["".join(list_dates_words[i]) for i in range(0, len(list_dates_words))]
	print(list_dates_words_fixed)

def process_stdin():
	input = [line.strip() for line in sys.stdin]
	text = ""
	for line in input:
		text = text + line
	return text
	
if __name__ == "__main__":
	main()