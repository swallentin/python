class DatePattern:
	
	def __init__(self, year, month, day, weekday = 0):
		self.year = year
		self.month = month
		self.day = day
		self.weekday = weekday
		
	def matches(self, dateToMatch):
		return (self.yearMatches(dateToMatch) and
				self.monthMatches(dateToMatch) and
				self.dayMatches(dateToMatch) and
				self.weekdayMatches(dateToMatch))
				
	def yearMatches(self, dateToMatch):
		if not self.year: return True
		return self.year == dateToMatch.year
	
	def monthMatches(self, dateToMatch):
		if not self.month: return True
		return self.month == dateToMatch.month
		
	def dayMatches(self, dateToMatch):
		if not self.day: return True
		return self.day == dateToMatch.day
	
	def weekdayMatches(self, dateToMatch):
		if not self.weekday: return True
		return self.weekday == dateToMatch.weekday()