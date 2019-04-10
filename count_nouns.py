from collections import Counter

c = Counter()

with open("/Users/jungwonchoi/Downloads/out.txt", "r") as f:
	for line in f:
		sp = line.split(" ")
		count = Counter(sp)
		c += count
with open("/Users/jungwonchoi/Downloads/freq_word.txt", "w") as out:
	for k,v in c.items():
		out.write('%s\t%s\n' % (k,v))