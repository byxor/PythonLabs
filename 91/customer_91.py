class Customer(object):
	
	def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
		self.name = name
		self.balance = balance
		self.addr_line1 = addr_line1
		self.addr_line2 = addr_line2
		self.addr_line3 = addr_line3
		
	def owes(self):
		return self.balance
	
	def __str__(self):
		return "{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: 0%\nAmount due: {:.2f}".format(self.name, self.addr_line1, self.addr_line2, self.addr_line3, self.balance, self.owes())
		
	
class ValuedCustomer(Customer):
	
	def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
		super(ValuedCustomer, self).__init__(name, balance, addr_line1, addr_line2, addr_line3)
		
	def owes(self):
		return self.balance*0.9
		
	def __str__(self):
		return "{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: 10%\nAmount due: {:.2f}".format(self.name, self.addr_line1, self.addr_line2, self.addr_line3, self.balance, self.owes())
		
# ------------------------

def main():

	c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
	c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon');
	c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry');

	print(c1)
	print(c2)
	print(c3)

if __name__ == '__main__':
	main()