from fnmatch import fnmatch, fnmatchcase

# Check if .txt ios present or not
# ------> *
if fnmatch('foo.txt', '*.txt'):
    print(".txt extended file is there")
# ------>Yes it a text file


# Check if any thing of ?oo.txt like loo,doo,too,foo
if fnmatch('foo.txt', '?oo.txt'):
    print("a sting with oo is present")


#  Check if string in range
if fnmatch('Dat45.csv', 'Dat[0-9]*'):
    print("After dat any decimal number ended are selected")


# Slect string start with dat and ends with .csv
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
csv_file = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(csv_file)
# ----->['Dat1.csv', 'Dat2.csv']

# fname is case sensitive in linux os
if fnmatch('foo.TXT', '?oo.txt'):
    print("fname is not case sensitve")
else:
    print("fname is case sensitive")


# For sure case sensitivity use fnamecase()
if fnmatchcase('foo.TXT', '?oo.txt'):
    print("fname is not case sensitve")
else:
    print("fname is case sensitive")
