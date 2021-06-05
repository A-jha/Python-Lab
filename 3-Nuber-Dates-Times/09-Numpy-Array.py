import numpy.linalg
import numpy as np

#==============================#
# Calculatiion On Large Matrix #
#==============================#

# Make a grid or 100 X 100 contains 0
zero_grid = np.zeros(shape=(100, 100), dtype=float)
print(zero_grid)
"""
Output:
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
"""


# Make a grid of 100 X 100 containing 1
one_grid = np.ones(shape=(100, 100), dtype=float)
print(one_grid)
"""
Output:
[[1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 ...
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]
 [1. 1. 1. ... 1. 1. 1.]]
"""


# Add 10 to zero grid and make ten_grid
ten_grid = zero_grid+10
print(ten_grid)
"""
Output
[[10. 10. 10. ... 10. 10. 10.]
 [10. 10. 10. ... 10. 10. 10.]
 [10. 10. 10. ... 10. 10. 10.]
 ...
 [10. 10. 10. ... 10. 10. 10.]
 [10. 10. 10. ... 10. 10. 10.]
 [10. 10. 10. ... 10. 10. 10.]]
"""


# sqrt of ten_grid
print(np.sqrt(ten_grid))
"""
Output:
[[3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]
 [3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]
 [3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]
 ...
 [3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]
 [3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]
 [3.16227766 3.16227766 3.16227766 ... 3.16227766 3.16227766 3.16227766]]
"""


# sin of ten_grid
print(np.sin(ten_grid))
"""
Output:
[[-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]
 [-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]
 [-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]
 ...
 [-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]
 [-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]
 [-0.54402111 -0.54402111 -0.54402111 ... -0.54402111 -0.54402111
  -0.54402111]]
"""


#========================#
# Indexin of numpy array #
#========================#

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
"""
Output:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""


# select Row-1
row1 = a[1]
print(row1)
# ---> output: [5,6,7,8]


# select col-1
col1 = a[:, 1]
print(col1)
# ---> output: [2, 6, 10]


# select a subregion
subArray = a[1:3, 1:3]
print(subArray)
"""
Output:
[[ 6  7]
 [10 11]]
"""


# change sub region of an array
a[1:3, 1:3] += 10
print(a)
"""
Output:
[[ 1  2  3  4]
 [ 5 16 17  8]
 [ 9 20 21 12]]
"""


# conditional assignment on array
# conditional assignment is similar to conditional operator
# if a<10 then a =a else a =10
a = np.where(a < 10, a, 10)
print(a)
"""
Output:
[[ 1  2  3  4]
 [ 5 10 10  8]
 [ 9 10 10 10]]
"""

#===========================#
# Linear Algebra On Matrix  #
#===========================#

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
"""
Output:
[[1 - 2  3]
 [0  4  5]
 [7  8 - 9]]
"""


# Transpose of a matrix
matrix_transpose = np.transpose(m)
print(matrix_transpose)
"""
Output:
[[1  0  7]
 [-2  4  8]
 [3  5 - 9]]
"""


# Second wat to transpose
matrix_transpose = matrix_transpose.T
print(matrix_transpose)
"""
Output:
[[1 - 2  3]
 [0  4  5]
 [7  8 - 9]]
"""

# inverse of matrix
matrix_inverse = m.I
print(matrix_inverse)
"""
Output:
[[ 0.33043478 -0.02608696  0.09565217]
 [-0.15217391  0.13043478  0.02173913]
 [ 0.12173913  0.09565217 -0.0173913 ]]
"""


# Create a vector and multiply
v = np.matrix([[2], [3], [4]])
print(v)
"""
Output:
[[2]
 [3]
 [4]]
"""

_m_x_v = m * v
print(_m_x_v)
"""
Output:
[[ 8]
 [32]
 [ 2]]
"""


# import numpy.linalg for more operations

# Determinat value of matrix m
det_m = numpy.linalg.det(m)
print(det_m)
# ----> Output: -229.99999999999983

# Eigen value of matrix
eigen_value = numpy.linalg.eigvalsh(m)


# solve x in mx = v
# x = v/m
x = numpy.linalg.solve(m, v)
print(x)
"""
[[0.96521739]
 [0.17391304]
 [0.46086957]]
"""

# v = mx
print(m*x)
"""
[[2]
 [3]
 [4]]
"""

# print v to verify
print(v)
"""
[[2]
 [3]
 [4]]
"""
