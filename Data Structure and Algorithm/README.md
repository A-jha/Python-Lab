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

##
