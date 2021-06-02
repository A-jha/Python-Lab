<h1 class="align-center">Data Structure and Algorithm</h1>
Python provides a variety of useful built-in data structures, such as lists, sets, and dictionaries.

## Unpacking a Sequence into Separate Variables

- Any sequence (or iterable) can be unpacked into variables using a simple assignment
  operation.

- The only requirement is that the number of variables and structure match
  the sequence.

```python
 p = (4,5)
 x,y = p
```

- To Many value to unpack error

```Python
p = (4,5,6)
#Through an error
x,y = p
```

- Not enough value to unpack

```python
p = (1,2)
#sequence does not matches
x,y,z = p
```

**Q. Write a python program that unpack a data such that date date of birth is unpacked too.**

```python
data = ["Avinash", 21, 90.1, (2000, 7, 26)]
```

- **Solution is inside `unpack.py` file**

## Unpacking Elements from Iterables of Arbitrary Length

### Python “star expressions”

- It is worth noting that the star syntax can be especially useful when iterating over a
  sequence of tuples of varying length.

```python
>>> *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

>>> trailing
[10, 8, 7, 1, 9, 5, 10]

>>> current
3
```

**Q. You are given a stack with n integers find head and tail of stack using unpack method**

- Solution in `star.py`

## Deque : Keeping the Last N Items

Keeping a limited history is a perfect use for a collections.deque .

- Deques are a generalization of stacks and queues
- the name is pronounced “deck” and is short for “double-ended queue”.
- Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

### Function of deque

- append(x)

- appendleft(x)
- clear()
- copy()
- count(x)
- extend(iterable)
- extendleft(iterable)
- insert(i,x)
- pop()
- popleft()
- remove()
- reverse()
- rotate(n=Rvalue)
  - Rvalue `< 0` rotale left
  - Rvalue `> 0` rotate right
- maxlen

## heapq : Finding the Largest or Smallest N Items

This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

The heapq module has two functions— nlargest() and nsmallest() —that do exactly what you want.

Function of heapq

- heappush(heap,item)

- heappop(heap)
- heapify(heap)
- nlargest(n,heap)
- nsmallest(n,heap)

```python
>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Implementing a Priority Queue

- **go to priorqueue.py**

## Mapping Keys to Multiple Values in a Dictionary

- A dictionary is a mapping where each key is mapped to a single value.
- If you want to map keys to multiple values, you need to store the multiple values in another container such as a list or set.

```python
#using list
d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
# using set
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}
```

- The choice of whether or not to use lists or sets depends on intended use.
  - Use a list if you want to preserve the insertion order of the items.
  - Use a set if you want to eliminate duplicates (and don’t care about the order).

## defaultdict from collection

### default dictionary with list

```python
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
```

### defaultdict with set

```python
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
"""
d = {
'a' : {1, 2},
'b' : {4}
}
"""
```

## Keeping dictionary in order

To control the order of items in a dictionary, you can use an OrderedDict from the collections module.

It exactly preserves the original insertion order of data when
iterating.

```python
from collections import OrderedDict

d = OrderedDict()

d['avi'] = 1
d['arp'] = 2
d['sam'] = 3
d['ravi'] = 4

for key in d:
    print(key, d[key])
```

- An OrderedDict can be particularly useful when you want to build a mapping that you may want to later serialize or encode into a different format.

### Create a json file with dict

```python
import json
from collections import OrderedDict

d = OrderedDict()
d['avi'] = 1
d['ravi'] = 12
d['kavi'] = 13
d['davi'] = 145
print(d)
print(json.dumps(d))
```

Output :
`OrderedDict([('avi', 1), ('ravi', 12), ('kavi', 13), ('davi', 145)])`<br>
`{"avi": 1, "ravi": 12, "kavi": 13, "davi": 145}`

## Calculating with dictionaries

### zip()

- it is often useful to invert the keys and values of the dictionary using zip() .
- In zip(arg1,arg2)
  - if we are sorting the sorted result will be based on arg1 not on arg2
  - hence in this case to find minimu we have to palce prices.values() as first args.

```Python
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
```

## Finding Commonalities in Two Dictionaries

- Find common in two dictionaries.

```python
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

```

## Naming a Slice

- slice take 3 args
  - start - index to start slicing
  - end - index to end slicing
  - step - gap betwwn index

```python
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Instead of doing manually we can set qa slic options
print(items[2:4])

# slice(start,end,step)

# a sile [2:4]
a = slice(2, 4)
# b slice [4: ]
b = slice(4, 8, 2)
print(items[a])
print(items[b])

# here b is an instance of slice so we can perform
# b.start
# b.end
# b.step

```

## Determining the Most Frequently Occurring Items in a Sequence

- Counter is very usefull tool

```Python
from collections import Counter

words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# return a dictionaries with word as key and cont as value
word_count = Counter(words)

# top three most frequent words
top_three = word_count.most_common(3)

# update the word list
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in morewords:
    word_count[word] += 1

# or we can update like
word_count.update(morewords)

#pop wiill remove that word from word_count dictionaries
print(word_count.pop('why'))

```

## Sorting a List of Dictionaries by a Common Key :: itemgetter

- itemgetter makes querying easy.

```python
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
```

## Grouping Records Together Based on a Field

The itertools.groupby() function is particularly useful for grouping data together.

## Filtering Sequence Elements

```python
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
```
