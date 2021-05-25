# sequence
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# filter the sequence such that no negetive item
print([n for n in mylist if n > 0])

# get items less than 0
print([n for n in mylist if n < 0])


# store results
positive_seq = [n for n in mylist if n > 0]

neg_seq = [n for n in mylist if n < 0]

# print neg_seq
print(neg_seq)
# --> it will return a context with data type and address where it is stored

# to print use iterators
for neg in neg_seq:
    print(neg)


# some list needs special treatment for that we have
# filter() function
values = ['1', '2', '3', '-', '+', '*']

# select all integer value


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


# Now we have many way eithe we can use iterators or use filter() function
ivals = list(filter(is_int, values))

print(ivals)
