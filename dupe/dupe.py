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
		md5s = {}
		for index, data in enumerate(strings):
			for line, twogram in enumerate(self.getMD5TwoGrams(data)):
				md5s.setdefault(twogram, []).append((index, {"startline":line}))

		matches = []
		for key in md5s:
			if len(md5s[key]) > 1:
				matches.append(md5s[key])
		return bool(list(matches)), matches