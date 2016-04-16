class Student(object):
	
	def __init__(self, surname, forename, sid, modlist=[]):
		self.surname = surname
		self.forename = forename
		self.sid = sid
		self.modlist = modlist
		
	def add_module(self, module):
		self.modlist.append(module)
		
	def del_module(self, module):
		try:
			self.modlist.remove(module)
		except:
			pass
			
	def print_details(self):
		print("ID: {}".format(self.sid))
		print("Surname: {}".format(self.surname))
		print("Forename: {}".format(self.forename))
		
		modules = ""
		for mod in self.modlist:
			modules = modules + mod + " "
		modules = modules[0:len(modules)-1]
		print("Modules: {}".format(modules))
		
def main():
	me = Student("Ibbotson", "Brandon", 15901157)
	me.add_module("MODULE1")
	me.add_module("CA19293142")
	me.add_module("bab")
	me.print_details()
	
if __name__ == "__main__":
	main()