# Number Dates And Times

## 1. Rounding Numerical values

When a value is exactly halfway between two choices, the behavior of round is to round to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.

```python
num1 = 1.5
num2 = 2.5
print(round(num1,0))
print(round(num2,0))
```

Output ---> 2 and 2

The number of digits given to round() can be negative, in which case rounding takes place for tens, hundreds, thousands, and so on.

```Python
num = 1234567
tens_of_num = round(num, -1)
```

## 2. Accurate Decimal Calculation

```python
a = 4.2
b = 2.1
print(a+b)
# ---> 6.300000000000001

print((a+b) == 6.3)
# ---> False
```

These errors are a “feature” of the underlying CPU and the IEEE 754 arithmetic performed by its floating-point unit. Since Python’s float data type stores data using the native representation, there’s nothing you can do to avoid such errors if you write your
code using float instances.

For error free result use **decimal module**

```Python
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
# ---> 6.3
print((a+b) == 6.3)
# ---> False
print((a+b) == Decimal('6.3'))
# ---> True
```

## Formatting Numbers for Output

```python
x = 1234.56789
# 1. two decimal places of accuracy
acc_2 = format(x, '0.2f')
print(acc_2)
# ---> 1234.57
```

## Working with Binary, Octal, and Hexadecimal Integers

To convert an integer into a binary, octal, or hexadecimal text string, use the bin(), oct(), or hex() functions.

```python
>>> x = 1234
>>> bin(x)
'0b10011010010'
>>> oct(x)
'0o2322'
>>> hex(x)
'0x4d2'
```

you can use the format() function if you don’t want the 0b , 0o , or 0x
prefixes to appear.

```python
>>> format(x, 'b')
'10011010010'
>>> format(x, 'o')
'2322'
>>> format(x, 'x')
'4d2'
```

**Plase read 3-binary_octal_hex.py file**

## Packing and Unpacking Large Integers from Bytes

Suppose your program needs to work with a 16-element byte string that holds a 128-bit integer value. For example:

```python
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
```

## Performing Complex-Valued Math

Complex numbers can be specified using the complex(real, imag) function or by floating-point numbers with a j suffix.

- pyhon math module has not complex support
- python cmath module has complec support
- numpy has good understanding of complex

```Python
a = complex(2, 3)
print(a)
# ---> (2+3j)
# 2 . To use complex number we can assign img part by suffix j
b = 3 + 4j
print(b)
# ---> (3+4j)
```

## Working with Infinity and NaNs

Python has no special syntax to represent these special floating-point values, but they can be created using float() .

```Python
a = float('inf')
print(a)
# 2. -ve infinity
b = float('-inf')
print(b)
# 3. nan
c = float('nan')
print(c)
# 4. chech if value is infinity math.isinf()
# import math
print(math.isinf(a))
# ---> True
# 5. check if value if nans math.isnan()
print(math.isnan(c))
# ---> True
```

## Calculating with Fractions

```python
from fractions import Fraction
# 1. Fraction module
a = Fraction(5, 4)
print(a)
# ---> 5/4
b = Fraction(4, 5)
print(b)
# ---> 4/5
```

## Calculating with Large Numerical Arrays

For any heavy computation involving arrays, use the NumPy library. The major feature
of NumPy is that it gives Python an array object that is much more efficient and better suited for mathematical calculation than a standard Python list.

```Python
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
```

- Here we can see that the array operations arte not proper mathematical.

## [Numpy Array](http://www.numpy.org)

NumPy provides a collection of “universal functions” that also allow for array operations.

Under the covers, NumPy arrays are allocated in the same manner as in C or Fortran.
Namely, they are large, contiguous memory regions consisting of a homogenous data
type. Because of this, it’s possible to make arrays much larger than anything you would normally put into a Python list.

```Python
import numpy as np
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
```

- One extremely notable aspect of NumPy is the manner in which it extends Python’s list indexing functionality—especially with multidimensional arrays.

```Python
# change sub region of an array
a[1:3, 1:3] += 10
print(a)
"""
Output:
[[ 1  2  3  4]
 [ 5 16 17  8]
 [ 9 20 21 12]]
"""
```

- Performing Linear algebra on matrix is a good application of numpy .
  _Please visit 09-Numpy file_

## Picking Things at Random

- to pick a random item out of a sequence, use random.choice()

```python
import random

# Rnadom basic
random_floating_num = random.random()
print(random_floating_num)
# ---> 0.9406677561675867

# get an int between 0 to 10
print(math.floor(random_floating_num*10))
# ---> 9
```

## Converting Days to Seconds, and Other Basic Time Conversions

### Timedelta

o perform conversions and arithmetic involving different units of time, use the date time module. For example, to represent an interval of time, create a timedelta instance.

```Python
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a+b
print(c)
# ---> Output: 2 days, 10: 30: 00
```

### datetime
