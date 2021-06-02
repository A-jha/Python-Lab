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

# sort the table based on uid
row_by_uid = sorted(rows, itemgetter('uid'))
print(row_by_uid)

# replacing itemgetter by lambda function
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(row_by_uid)

# select row with minimum user id
min(rows, key=itemgetter('uid'))
# select row with max user id
max(rows, key=itemgetter('uid'))
