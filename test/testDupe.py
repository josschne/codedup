import unittest
from dupe import dupe

class testBasicMatching(unittest.TestCase):

	def setUp(self):
		self.my_dupe = dupe.dupe()

	def testTwoDifferentLinesAreNotDuplicates(self):
		result = self.my_dupe.dupe('Hello\nHello\n', 'World\nWorld\n')
		self.assertEqual(result, False)

	def testTwoEqualLinesAreDuplicates(self):
		result = self.my_dupe.dupe('Hello\nWorld\n', 'Hello\nWorld\n')
		self.assertEqual(result, True)

	def testFindDuplicateInMultilineSource(self):
		result = self.my_dupe.dupe('Brave\nNew\nWorld\n', 'New\nWorld\n')
		self.assertEqual(result, True)

	def testFindDuplicateInMultilineSourceAndTarget(self):
		result = self.my_dupe.dupe('Brave\nNew\nWorld\nPeace\n', 'World\nPeace\n')
		self.assertEqual(result, True)

	def testFindDuplicateInTestFiles(self):
		result = self.my_dupe.dupe(open('testFileA.txt').read(), open('testFileB.txt').read())
		self.assertEqual(result, True)

	def testFindDuplicatesInThree(self):
		result = self.my_dupe.dupe(open('testFileA.txt').read(), open('testFileB.txt').read(), open('testFileC.txt').read())
		self.assertEqual(result, True)

