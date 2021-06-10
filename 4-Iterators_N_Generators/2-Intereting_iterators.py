#======================#
# Iterating in reverse #
#======================#

from os import path


a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
"""
4
3
2
1
"""

#===========================#
# Print a file in backwards #
#===========================#
f = open('test.txt',  mode='r', encoding="UTF-8")
print(f.read())

for letter in reversed(list(f)):
    print(letter, end='')
