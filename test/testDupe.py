import unittest
from dupe import dupe

class testFunctions(unittest.TestCase):

	def testStart(self):
		my_dupe = dupe.dupe()
		result = my_dupe.dupe('Hello', 'World')
		self.assertTrue(result == False)