#!/usr/bin/env python
# encoding: utf-8
"""
FooTests.py

Created by stephan.wallentin@gmail.com on 2011-04-12.
Copyright (c) 2011 Stephan Wallentin. All rights reserved.
"""
import unittest
import datetime

Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday = range(0, 7)

class YearPattern:
	
	def __init__(self, year):
		self.year = year

	def matches(self, dateToMatch):
		return self.year == dateToMatch.year

class MonthPattern:

    def __init__(self, month):
    	self.month = month
   
    def matches(self, dateToMatch):
    	return self.month == dateToMatch.month
     
class DayPattern:
   
	def __init__(self, day):
		self.day = day
   
	def matches(self, dateToMatch):
		return self.day == dateToMatch.day

class WeekDayPattern:

	def __init__(self, weekday):
		self.weekday = weekday

	def matches(self, dateToMatch):
		return self.weekday == dateToMatch.weekday()

class LastWeekDayPattern():

	def __init__(self, weekday):
		self.weekday = weekday
		
	def matches(self, dateToMatch):
		nextWeekFromDateToMatch = dateToMatch + datetime.timedelta(7)
		return self.weekday == date.weekday() and nextWeekFromDateToMatch.month != dateToMatch.month

class NthWeekdayPattern():
	
	def __init__(self, n, weekday):
		self.n = n
		self.weekday = weekday
		
	def matches(self, dateToMatch):
		if( self.weekday != dateToMatch.weekday() ):
			return False;
		
		return self.n == self.getWeekdayNumber(dateToMatch)
	
	def getWeekdayNumber(self, dateToMatch):
		n = 1
		while True:
			previousDate = dateToMatch - datetime.timedelta(7*n)
			if( previousDate.month == dateToMatch.month):
				n+=1
			else:
				break
		return n;
		
class CompositePattern:
	
	def __init__(self):
		self.patterns = []
	
	def add(self, patternToAdd):
		self.patterns.append(patternToAdd)

	def matches(self, dateToMatch):
		for pattern in self.patterns:
			if not pattern.matches(dateToMatch):
				return False;
			return True;

class NewTests(unittest.TestCase):
	
	def testYearMatches(self):
		yp = YearPattern(2004)
		d = datetime.date(2004,9,29)
		self.failUnless(yp.matches(d))

	def testYearDoesNotMatch(self):
		yp = YearPattern(2004)
		d = datetime.date(2004+1,9,29)
		self.failIf(yp.matches(d))
	
	def testMonthMatches(self):
		mp = MonthPattern(9)
		d = datetime.date(2004,9,29)
		self.failUnless(mp.matches(d))

	def testMonthDoesNotMatch(self):
		mp = MonthPattern(9)
		d = datetime.date(2004,9+1,29)
		self.failIf(mp.matches(d))	
		
	def testDayMatches(self):
		dp = DayPattern(29)
		d = datetime.date(2004,9,29)
		self.failUnless(dp.matches(d))

	def testDayDoesNotMatch(self):
		dp = DayPattern(29)
		d = datetime.date(2004,9,29+1)
		self.failIf(dp.matches(d))		

	def testWeekDayMatches(self):
		wp = WeekDayPattern(2)
		d = datetime.date(2004,9,29)
		self.failUnless(wp.matches(d))

	def testWeekDayDoesNotMatch(self):
		wp = WeekDayPattern(2)
		d = datetime.date(2004,9,29+1)
		self.failIf(wp.matches(d))

	def testCompositeMatches(self):
		cp = CompositePattern()
		cp.add(YearPattern(2004))
		cp.add(MonthPattern(9))
		cp.add(DayPattern(29))
		d = datetime.date(2009,9,29)
		self.failIf(cp.matches(d))
		
	def testCompositeWithoutYearMatches(self):
		cp = CompositePattern()
		cp.add(MonthPattern(4))
		cp.add(DayPattern(10))
		d = datetime.date(2004,04,10)
		self.failUnless(cp.matches(d))

class PatternTest(unittest.TestCase):
	
	def setUp(self):
		self.dateToTest = datetime.date(2004, 4,29)
		
	def testYearMatches(self):
		yp = YearPattern(2004)
		self.failUnless(yp.matches(self.dateToTest))

	def testYearDoesNotMatch(self):
		yp = YearPattern(2003)
		self.failIf(yp.matches(self.dateToTest))

class LastWeekDayPatternTest(unittest.TestCase):
	
	def setUp(self):
		self.pattern = LastWeekDayPattern(Wednesday)
	
	def testLastWednesdayMatches(self):
		lastWednesdayOfSeptember2004 = datetime.date(2004,9,29)
		self.failUnless(self.pattern.matches(lastWednesdayOfSeptember2004))
		
	def testLastWednesdayDoesNotMatch(self):
		firstWednesdayOfSeptember2004 = datetime.date(2004,9,1)
		self.failIf(self.pattern.matches(firstWednesdayOfSeptember2004))

class NthWeekdayPatternTests(unittest.TestCase):
	
	def setUp(self):
		self.pattern = NthWeekdayPattern(1, Wednesday)
		
	def testMatches(self):
		firstWednesdayofSeptember2004 = datetime.date(2004, 9, 1)
		self.failUnless(self.pattern.matches(firstWednesdayofSeptember2004))

	def testNotMatches(self):
		secondWednesdayOfSeptember2004 = datetime.date(2004, 9, 8)
		self.failIf(self.pattern.matches(secondWednesdayOfSeptember2004))
		
		

if __name__ == '__main__':
	unittest.main()