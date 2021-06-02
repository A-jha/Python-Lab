import re
line = 'asdf lkjh;          aqswde,lploli,         foo'


print(line)
# ----->asdf lkjh;          aqswde,lploli,         foo


splitedLine = re.split(r'[;\s]\s*', line)
print(splitedLine)
# -------->['asdf', 'lkjh', 'aqswde,lploli,', 'foo']
