import sys

def main():
	createMonthsDict()
	dates = processSTDIN()
	shortDates = [getShortDate(date) for date in dates if True]
	
	for shortDate in shortDates:
		print(shortDate)
	
def createMonthsDict():
	global months
	months = {}
	months["January"] = 1
	months["February"] = 2
	months["March"] = 3
	months["April"] = 4
	months["May"] = 5
	months["June"] = 6
	months["July"] = 7
	months["August"] = 8
	months["September"] = 9
	months["October"] = 10
	months["November"] = 11
	months["December"] = 12
	
def getShortDate(date):
	compv = date.split(" ")
	day = formatDay(compv[0])
	month = formatMonth(compv[1])
	year = formatYear(compv[2])
	return "{}/{}/{}".format(day, month, year)
	
def formatDay(day):
	#lastChar = day[len(day)-1]
	#if lastChar in ["1"]:
	#	return day + "st"
	#if lastChar in ["2"]:
	#	return day + "nd"
	#if lastChar in ["3"]:
	#	return day + "rd"
	#if lastChar in ["4","5","6","7","8","9","0"]:
	#	return day + "th"
	return day

def formatMonth(month):
	global months
	return months[month]
	
def formatYear(year):
	length = len(year)
	return year[length-2:length]
	

def processSTDIN():
	words = []
	for line in sys.stdin:
		words.append(line.strip())
	return words
	
if __name__ == "__main__":
	main()