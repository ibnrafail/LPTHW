tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

import time
import sys

backslash_state = ['|', '\\', '-',  '/', '|', '\\', '-', '/']
j = 0
for i in range(1, 101):
    time.sleep(0.01)
    sys.stdout.write("\r[%3d]%%[%s]" % (i, backslash_state[j]))
    sys.stdout.flush()
    j += 1
    if j >= len(backslash_state):
    	j = 0
print ""
while True:
	for i in ["/","- ","|","\\","|"]:
		time.sleep(0.1)
		sys.stdout.write("\r%s" % i)
		sys.stdout.flush()
