from operator import itemgetter

# Database
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# sort the table based on fname
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
"""
Output:
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
"""
# sort the table based on uid
row_by_uid = sorted(rows, key=itemgetter('uid'))
print(row_by_uid)

"""
Output:
[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
"""

# replacing itemgetter by lambda function
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)

"""
Output:
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
"""

rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(row_by_uid)

"""
Output:
[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
"""

# select row with minimum user id
print(min(rows, key=itemgetter('uid')))

"""
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
"""
# select row with max user id
print(max(rows, key=itemgetter('uid')))

"""
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
"""
