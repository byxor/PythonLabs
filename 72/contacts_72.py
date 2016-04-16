class Contact(object):
	
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email
		
	def __str__(self):
		if self.name == None:
			return ("{} : No such contact".format(name))
		return ("{} {} {}").format(self.name, self.phone, self.email)
	
class ContactList(object):
	
	def __init__(self, dictionary=None):
		if dictionary == None:
			dictionary = {}
		self.contact_dictionary = dictionary
		
	def add_contact(self, contact):
		self.contact_dictionary[contact.name] = contact
		
	def del_contact(self, name):
		try:
			del self.contact_dictionary[name]
		except KeyError:
			pass
	
	def get_contact(self, name):
		try:
			return self.contact_dictionary[name].__str__()
		except KeyError:
			return "{} : No such contact".format(name)
			
	def __str__(self):
		
		sorted_contacts = []
		
		length = len(self.contact_dictionary)
		
		for i in range(0, length):
			lowest_alph_index = 0
			for j in range(i+1, length):
				if self.contact_dictionary[]
			
			
		string = "Contact list\n------------"
		for contact in sorted_contacts:
			string = string + "\n{}".format(contact[1])
		return string

# DRIVER CODE ---------------------------------------
		
import sys

def main():
	cl = ContactList()
	for line in sys.stdin:
		lad = line.strip().split()
		c = Contact(lad[0], lad[1], lad[2])
		cl.add_contact(c)

	print(cl.get_contact('Jimmy'))
	print(cl.get_contact('Mary'))

	print(cl)
	cl.del_contact('Maggie')
	cl.del_contact('Maggie')

	c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
	cl.add_contact(c)
	print(cl)
	
if __name__ == "__main__":
	main()