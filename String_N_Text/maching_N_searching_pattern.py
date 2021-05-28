import re
# Matching and Searching for Text Patterns

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
text == 'yeah'
# ------>False

# Match at start or end
text.startswith('yeah')
# ------->True
text.endswith('no')
# ------>False

# search for location of first ocurance
pos = text.find('no')
print(pos)

#####  Some Complex Pattern ######

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
#import re
# Simple matching: \d+ means one or more digits
if re.match(r'\d+/\d+/\+d+', text1):
    print("yes")
else:
    print("No")
# ------>Yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print("No")
# -------->No

"""
match() always tries to find the match at the start of a string. If you want to search text
for all occurrences of a pattern, use the findall() method instead.
"""
datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 05/27/2021.  bday starts 05/21/2000.'

print(datepat.findall(text))

"""
When defining regular expressions, it is common to introduce capture groups by en‐
closing parts of the pattern in parentheses.
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('05/27/2021')
print(m)
# -----> Output: re.Match object; span=(0, 10), match='05/27/2021'>

# extract the content of each group
print(m.group(0))
# 05/27/2021

print(m.group(1))
# -------->5

print(m.group(2))
# -------->27

print(m.group(3))
# -------->2021

print(m.groups())
# -------->('05','27','2021')

month, day, year = m.groups()
print(month)
# ----->05
print(day)
# ----->27
print(year)
# ----->2021

# Find all matches (notices spliting into tuples)
print(text)
# ------> Today is 05/27/2021.  bday starts 05/21/2000.

print(datepat.findall(text))
# ------>[('05', '27', '2021'), ('05', '21', '2000')]

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
# 2021-05-27
# 2000-05-21
