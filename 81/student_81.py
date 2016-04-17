from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
			   'CA106': Module('CA106', 'Web Design', 5),
			   'CA115': Module('CA115', 'Digital Innovation', 5),
			   'CA116': Module('CA116', 'Computer Programming I', 10),
			   'CA117': Module('CA117', 'Computer Programming II', 10),
			   'CA169': Module('CA169', 'Networks and Internet', 5),
			   'CA170': Module('CA170', 'Operating Systems', 5),
			   'CA172': Module('CA172', 'Problem Solving', 5),
			   'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

	def __init__(self, idnum, surname, firstname, mods=CA1_MODULES):
		self.__idnum = idnum
		self.__surname = surname
		self.__firstname = firstname
		self.__mods = mods
		self.__marks = {code: 0 for code in self.__mods.keys()}

	def __str__(self):
		name = '{} : {} {}'.format(self.__idnum,
								   self.__firstname,
								   self.__surname)
		uline = '-' * len(name)
		results =  '\n'.join([code + ' : ' + self.__mods[code].title +
							  ' : ' + str(self.__marks[code])
							  for code in sorted(self.__mods.keys())])
		pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
		if self.passed():
			outcome = 'Pass'
		elif self.passed_by_compensation():
			outcome = 'Pass by compensation'
		else:
			outcome = 'Fail'

		return '\n'.join([name, uline, results, pm, outcome])

	def add_mark(self, modcode, mark):
		self.__marks[modcode] = mark

	def precision_mark(self):
		precision_mark = 0
		overall_creds = 0
		for item in self.__marks.items():
			precision_mark += item[1] * self.__mods[item[0]][2]
			overall_creds += self.__mods[item[0]][2]
		precision_mark /= overall_creds
		return precision_mark

	def passed(self):
		return (self.precision_mark() >= 60)

	def passed_by_compensation(self):
		condition1 = (self.precision_mark() >= 45)
		condition2 = (get_failed_credits() <= 1/6)
		condition3 = False
		return (condition1 and condition2 and condition3)
		
	def get_failed_credits(self):
		total_credits = 0
		for item in self.__mods().items():
			total_credits += item[1][2]
		
		
# ---------------------

def main():

	s1 = Student(15334499, 'Jones', 'Zoe')
	s1.add_mark('CA103', 71)
	s1.add_mark('CA106', 65)
	s1.add_mark('CA115', 84)
	s1.add_mark('CA116', 85)
	s1.add_mark('CA117', 70)
	s1.add_mark('CA169', 68)
	s1.add_mark('CA170', 74)
	s1.add_mark('CA172', 90)
	s1.add_mark('MS121', 50)
	

	s2 = Student(15667755, "Brent", "Tom")
	s2.add_mark('CA103', 55)
	s2.add_mark('CA106', 35)
	s2.add_mark('CA115', 70)
	s2.add_mark('CA116', 64)
	s2.add_mark('CA117', 66)
	s2.add_mark('CA169', 50)
	s2.add_mark('CA170', 55)
	s2.add_mark('CA172', 60)
	s2.add_mark('MS121', 35)

	s3 = Student(15112277, 'Brody', 'Joe')
	s3.add_mark('CA103', 35)
	s3.add_mark('CA106', 35)
	s3.add_mark('CA115', 60)
	s3.add_mark('CA116', 60)
	s3.add_mark('CA117', 60)
	s3.add_mark('CA169', 60)
	s3.add_mark('CA170', 60)
	s3.add_mark('CA172', 60)
	s3.add_mark('MS121', 60)

	print(s1)
	print(s2)
	print(s3)
						
if __name__ == '__main__':
	main()