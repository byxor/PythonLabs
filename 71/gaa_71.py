class Score(object):
	
	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points
		self.truepoints = points + goals*3
		
	def greater_than(self, s):
		return self.truepoints > s.truepoints
		
	def less_than(self, s):
		return self.truepoints < s.truepoints
		
	def equal_to(self, s):
		return self.truepoints == s.truepoints