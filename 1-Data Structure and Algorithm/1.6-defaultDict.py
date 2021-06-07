from collections import defaultdict

# Default dictionary with List of items
d = defaultdict(list)
# Here we have a as key and a list associated with it as pair.
"""
d = {
    'a' = [1,2],
    'b' = [4]
}
"""
# A dict with two key a and b
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(5)
print(d['a'])
# ---> [1, 2]

print(d['b'])
# ---> [4, 5]

# 2.__len__ will tells us the lenth of collections
print(d.__len__())
# ---> 2


# 3. We can pop with the key
# print(d.pop())
# ---> TypeError: pop expected at least 1 argument, got 0
print(d.pop('b'))
# ---> [4, 5]


# 4.
x = [1, 2, 3, 4]
d.update(a=x)
print(d['a'])
# ---> [1, 2, 3, 4]

# 5.Remove all items from dict
# d.clear()
