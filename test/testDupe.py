import unittest
from dupe import dupe

class testBasicMatching(unittest.TestCase):

	def setUp(self):
		self.my_dupe = dupe.dupe()

	def testTwoDifferentLinesAreNotDuplicates(self):
		result, _ = self.my_dupe.dupe('Hello\nHello\n', 'World\nWorld\n')
		self.assertEqual(result, False)

	def testTwoEqualLinesAreDuplicates(self):
		result, _ = self.my_dupe.dupe('Hello\nWorld\n', 'Hello\nWorld\n')
		self.assertEqual(result, True)

	def testFindDuplicateInMultilineSource(self):
		result, _ = self.my_dupe.dupe('Brave\nNew\nWorld\n', 'New\nWorld\n')
		self.assertEqual(result, True)

	def testFindDuplicateInMultilineSourceAndTarget(self):
		result, _ = self.my_dupe.dupe('Brave\nNew\nWorld\nPeace\n', 'World\nPeace\n')
		self.assertEqual(result, True)

	def testFindDuplicateInTestFiles(self):
		result, _ = self.my_dupe.dupe(open('testFileA.txt').read(), open('testFileB.txt').read())
		self.assertEqual(result, True)

	def testFindDuplicatesInThree(self):
		result, _ = self.my_dupe.dupe(open('testFileA.txt').read(), open('testFileB.txt').read(), open('testFileC.txt').read())
		self.assertEqual(result, True)

	def testDuplicateLineNumbersAreReported(self):
		result, matches = self.my_dupe.dupe('Hello\nWorld\n', '1\n2\nHello\nWorld\n5\n6\n')
		self.assertEqual(matches, [ [(0,{"startline":0}), (1,{"startline":2})] ])
