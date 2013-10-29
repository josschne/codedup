import unittest
from dupe import dupe

class testBasicMatching(unittest.TestCase):

	def setUp(self):
		self.my_dupe = dupe.dupe()

	def testTwoDifferentLinesAreNotDuplicates(self):
		result = self.my_dupe.dupe('Hello', 'World')
		self.assertEqual(result, False)

	def testTwoEqualLinesAreDuplicates(self):
		result = self.my_dupe.dupe('Hello', 'Hello')
		self.assertEqual(result, True)
