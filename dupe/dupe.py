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

	def dupe(self, *strings):
		md5s = []
		for data in strings:
			md5s.append(self.getMD5TwoGrams(data))
			
		matches = set(md5s[0])
		for twograms in md5s[1:]:
			matches = matches & set(twograms)
		return bool(list(matches))