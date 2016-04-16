class Contact(object):
	
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email
	
	def __str__(self):
		return "{} {} {}".format(self.name, self.phone, self.email)
		

class ContactList(object):

	def __init__(self):
		self.contacts = {}
		
	def __str__(self):
		return get_sorted_string(self.contacts)
		
	def del_contact(self, name):
		try:
			self.contacts.pop(name, None)
		except KeyError:
			pass
		
	def add_contact(self, c):
		self.contacts[c.name] = c
		
	def get_contact(self, name):
		try:
			return self.contacts[name]
		except KeyError:
			return "{} : No such contact".format(name)
		
# -------------------------------

def partition(itemlist, start, end):
	pivot = itemlist[end]
	pIndex = start
	i = start
	
	while i < end:
		if itemlist[i][0] <= pivot[0]:
			itemlist[i], itemlist[pIndex] = itemlist[pIndex], itemlist[i]
			pIndex += 1
		i += 1
	
	itemlist[i], itemlist[pIndex] = itemlist[pIndex], itemlist[i]
	return pIndex
	
def quicksort(itemlist, start, end):
	if start >= end:
		return
	pIndex = partition(itemlist, start, end)
	quicksort(itemlist, start, pIndex-1)
	quicksort(itemlist, pIndex+1, end)

def get_sorted_string(contactlist):
	itemlist = list(contactlist.items())
	quicksort(itemlist, 0, len(itemlist)-1)
	s = "Contact list\n------------\n"
	for i in range(0, len(itemlist)):
		s += str(itemlist[i][1])
		if i<len(itemlist)-1:
			s += "\n"
	return s

# -------------------------------

import sys

def main():
	cl = ContactList()
	for line in sys.stdin:
		[name, phone, email] = line.strip().split()
		c = Contact(name, phone, email)
		cl.add_contact(c)

	print(cl.get_contact('Jimmy'))
	print(cl.get_contact('Mary'))

	print(cl)
	cl.del_contact('Maggie')
	cl.del_contact('Maggie')

	c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
	cl.add_contact(c)
	print(cl)

if __name__ == '__main__':
	main()