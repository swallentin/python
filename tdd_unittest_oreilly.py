import unittest

def IsOdd(number):
	return number % 2 == 1
	
class IsOddTest(unittest.TestCase):
	
	def testOne(self):
		self.failUnless(IsOdd(1))
		print('testOne')
		
	def testTwo(self):
		self.failIf(IsOdd(2))
		print('testTwo')
		
def main():
	unittest.main()
	
if( __name__ == '__main__'):
	main()