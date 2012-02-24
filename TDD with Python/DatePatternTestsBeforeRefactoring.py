class PatternsTests(unittest.TestCase):
	
	def testMatches(self):
		p = DatePattern(2004,9,28)
		d = datetime.date(2004,9,28)
		self.failUnless(p.matches(d))

	def testMatchesFalse(self):
		p = DatePattern(2004,9,28)
		d = datetime.date(2004,9,29)
		self.failIf(p.matches(d))
	
	def testMatchesYearAsWildCard(self):
		p = DatePattern(0, 4, 10)
		d = datetime.date(2005, 4, 10)
		self.failUnless(p.matches(d))
		
	def testMatchesYearAndMonthAsWildCard(self):
		p = DatePattern(0,0,1)
		d = datetime.date(2004,10,1)
		self.failUnless(p.matches(d))
	
	def testMatchesWeekday(self):
		p = DatePattern(0,0,0,2) # 2 is wednesday
		d = datetime.date(2004,9,29)
		self.failUnless(p.matches(d))
		
	def testMatchesWeekdayFalse(self):
		p = DatePattern(0,0,0,3 ) # 2 is wednesday
		d = datetime.date(2004,9,29)
		self.failIf(p.matches(d))