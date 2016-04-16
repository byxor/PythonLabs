class Point(object):
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __str__(self):
		return "({}, {})".format(self.x, self.y)
		
#end class

class Segment(object):
	
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	def midpoint(self):
		midx = (self.p1.x + self.p2.x)/2
		midy = (self.p1.y + self.p2.y)/2
		return Point(midx, midy)
		
	def length(self):
		difx = self.p2.x - self.p1.x
		dify = self.p2.y - self.p1.y
		return (difx**2 + dify**2)**0.5
		
#end class

class Circle(object):

	def __init__(self, p, r):
		self.r = r
		self.p = p
		
	def overlaps(self, other):
		segment = Segment(self.p, other.p)
		return (segment.length() < (self.r + other.r))
		
#end class

def main():
	p1 = Point()
	p2 = Point(5, 5)
	s1 = Segment(p1, p2)
	s2 = Segment(p2, p1)
	c1 = Circle(p1, 5)
	c2 = Circle(p2, 2)
	c3 = Circle(p1, 2)

	print(p1)
	print(p2)
	print(s1.midpoint())
	print(s2.midpoint())
	print(c1.overlaps(c2))
	print(c2.overlaps(c1))
	print(c1.overlaps(c3))
	print(c3.overlaps(c2))

if __name__ == '__main__':
	main()










































