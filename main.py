from dupe import dupe
import sys

main = dupe.dupe()
filenames = sys.argv[1:]
strings = map(lambda file: open(file).read(), filenames)
result, match_info = main.dupe(*strings)
print match_info
for match in match_info:
	print "Matching lines found in: "
	for file_index, info in match:
		print "  File: %s at line %s" % (filenames[file_index], info["startline"])