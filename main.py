from dupe import dupe
import sys

main = dupe.dupe()
filenames = sys.argv[1:]
strings = map(lambda file: open(file).read(), filenames)
result = main.dupe(*strings)
if result:
	print "Match found!"
else:
	print "No match found!"