class Demo(object):
	"""docstring for Demo"""
	def __init__(self, arg):
		super(Demo, self).__init__()
		self.arg = arg
		
		
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
def ThisIsAProperty():
    doc = "The ThisIsAProperty property."
    def fget(self):
        return self._ThisIsAProperty
    def fset(self, value):
		self._ThisIsAProperty = value
    def fdel(self):
        del self._ThisIsAProperty
    return locals()
ThisIsAProperty = property(**ThisIsAProperty())