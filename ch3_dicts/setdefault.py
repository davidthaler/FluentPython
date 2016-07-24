import sys
import re

WORD = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD.finditer(line):
            word = match.group()
            col_no = match.start() + 1
            loc = (line_no, col_no)
            index.setdefault(word, []).append(loc)

for word in sorted(index, key=str.upper):
    print(word, index[word])
