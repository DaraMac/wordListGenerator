#!/usr/bin/env python3

import string
from collections import Counter

def line_prep(line):
	punctuation = string.punctuation + '«»'
	line = line.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
	return line.lower()

# inclusive
start_year = 2001
end_year = 2018

with open('it.txt') as f:
	italian = frozenset(line.rstrip('\n') for line in f)

words = Counter()

for year in range(start_year, end_year + 1):
	with open(str(year) + '.txt') as f:
		for line in f:
			for word in line_prep(line).split():
				if word.isalpha() and word in italian:
					words[word] += 1

with open('frequencyList.txt', 'w') as f:
	print(len(words), file=f)
	for word, freq in words.most_common():
		print(word, freq, file=f)
