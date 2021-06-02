import os
filename = 'spam.txt'

if filename.endswith('.txt'):
    print("A text file is found")

if filename.startswith('spam'):
    print("A spam is present")

"""
Output:
A text file is found
A spam is present
"""

# import list of dirs in working dir
filenames = os.listdir(
    '/home/avinashjha/Desktop/Projects/Python/Python-Lab/String_N_Text')

# print filenames present in  given dirs
print(filenames)
# ------>['2-start_end_str.py', 'README.md', '1-split.py']

# print file name ending with .py
pythonFile = [name for name in filenames if name.endswith('.py')]
print(pythonFile)
# --------->['2-start_end_str.py', '1-split.py']

# check if any .md file is there
if(any(name.endswith('.md') for name in filenames)):
    print(".md extended file is there")
# -------> .md extended file is there


# check if url end wirh org and stars with http
url = 'http://www.python.org'
if url.endswith('.org') & url.startswith('http'):
    print("I think url is valid")
# --------->I think url is valid
