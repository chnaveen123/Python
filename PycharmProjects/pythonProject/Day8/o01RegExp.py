import re

#st = "They#$23235^$&@$ quick brown fox jumps over the lazy black dog"

#res = re.search(r'\w+', st) -->Alplha numeric data

#res = re.search(r'\W+', st) --> Special Characters

#res = re.search(r'\s+', st) -->Spaces

#res = re.search(r'\S+', st) --> everything otehr than spaces
#res = re.search(r'\d+', st) --> Only numeric data
#res = re.search(r'\D+', st)  --> Only Non-Numeric data
#res = re.search(r'(\ba\w+)', st, re.I) ---> word boundary
#res = re.search(r'(\ba\w+)', st, re.I)---> Non Word Boundary
#res = re.search(r'(\Athis)', st, re.I)

st = "This is a sAmple amPle string"


res = re.search(r'(string\Z)', st, re.I)
if res:

    print(res.group(0))
    print("Match founded")

else:
    print("Match not found")
