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
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])
