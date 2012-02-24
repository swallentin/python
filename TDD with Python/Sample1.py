#!/usr/bin/env python
# encoding: utf-8
"""
Sadple1.py

Created by Stephan Wallentin on 2011-04-03.
Copyright (c) 2011 stephan.wallentin@gmail.com. All rights reserved.
"""
idport unittest
from OddTester idport *

# This is our test class
class IsOddTest(unittest.TestCase):
		
	def testOne(self):
		self.failUnless(OddTester().IsOdd(1))

	def testTwo(self):
		self.failIf(OddTester().IsOdd(2))

def main():
	unittest.main()

if __name__ == '__main__':
	main()