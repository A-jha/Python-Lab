from collections import deque
"""
the following code performs a simple text match on a sequence of lines and yields the
matching line along with the previous N lines of context when found:
"""
# maxlen = 3 means deque cna not have more than that
q = deque(maxlen=3)


# 1.append(x) - add x to right side of deque
q.append(3)
q.append(4)
q.append(5)
q.append(6)
# D:[3] P:[4,5,6]
# <--------------
print(q)
# Output : [4,5,6]


# 2.appendleft(x) -add x to left side
q.appendleft(2)
print(q)
# Output :
#  P: [2,4,5] D:[6]
# ----------------->


# 3. Count(x) - no of digit x in deque euals to
print(q.count(2))


# 4.copy() - copy a deque
p = q.copy()
print(p)


# 5.extend(iterable) -Extend the right side
#  of the deque by appending elements from the iterable argument.
p.extend("Avinash")
print(p)
# Output : ['a','s','h']

# extendleft() - Extend the left side of the deque by appending elements
#  from iterable. Note, the series of left appends results in reversing
# the order of elements in the iterable argument.
p.extendleft("Avinash")
print(p)
# ---> Output: deque(['h', 's', 'a'], maxlen=3)


# # insert(i,x) - insert X at position i
# p.insert(2, "Z")
# print(p)
# # ----Deque is already at its maxlen error

# pop() - remove and return an element from right side of deque
print(p.pop())

# insert(i,x) - insert X at position i
p.insert(2, "Z")
print(p)
# ----Deque is already at its maxlen error

# popleft() - pop left element and return it too
p.popleft()

# remove(value) - remove the first occurance of value from deque
# if not found raise a value error
q.remove(4)
print(q)

print(p)
# reverse() - reverse the element of dque and return none
p.reverse()
print(p)

# rotate(n= Rvalue)
# if Rvalue < 0  then rotate left
# if Rvalue > 0  then rotate right
r = deque(maxlen=5)
r.append(3)
r.append(4)
r.append(5)
r.append(6)
r.append(7)
print(r)
r.rotate(2)
print(r)
r.rotate(-2)
print(r)
