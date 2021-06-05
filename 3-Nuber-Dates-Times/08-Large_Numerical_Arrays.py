import numpy as np

# Python List

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

# constant multiplication
print(x*2)
# ---> Output: [1, 2, 3, 4, 1, 2, 3, 4]

# z = x+10
# TypeError: can only concatenate list(not "int") to list

z = x+y
print(z)
# --->Output:[1, 2, 3, 4, 5, 6, 7, 8]


# Numpy Arrays
# import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

# constant multiplication
print(ax*2)
# ---> Output: [2 4 6 8]


# Add Constant
print(ax+10)
# ---> Output: [11 12 13 14]


# Add two array
_sum = ax+ay
print(_sum)
# ---> Output: [ 6  8 10 12]


# multiply two array
_prod = ax*ay
print(_prod)
# ---> Output: [ 5 12 21 32]
