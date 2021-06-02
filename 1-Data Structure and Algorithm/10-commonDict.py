a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find keys in common
print(a.keys() & b.keys())
# --->y, x is common

# find keys in a that are not in b
a.keys() - b.keys()
# ---->z


# find keys value pair in common
print(a.items() & b.items())

# make a new dictionaries with certain key removed
c = {key: a[key] for key in a.keys()-{'z', 'w'}}
print(c)
