from hashlib import md5

class dupe:

	def getMD5TwoGrams(self, inputString):
		md5_two_grams = []
		lines = inputString.split()
		for i in xrange(0, len(lines)-1):
			line_hash = md5()
			line_hash.update(lines[i])
			line_hash.update(lines[i+1])
			md5_two_grams.append(line_hash.digest())
		return md5_two_grams

	def dupe(self, first, second):
		first_md5s = self.getMD5TwoGrams(first)
		second_md5s = self.getMD5TwoGrams(second)

		matches = list(set(first_md5s) & set(second_md5s))
		return bool(matches)