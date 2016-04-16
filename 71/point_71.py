class Point(object):
	
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y
		
	def reflect(self):
		self.x = -self.x
		self.y = -self.y
		
	def distance(self, p):
		xDist = self.x - p.x
		yDist = self.y - p.y
		return (xDist**2 + yDist**2)**0.5