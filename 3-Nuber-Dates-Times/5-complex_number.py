
# 1. To use complex number we can use complex(real,img) function
import math
import cmath
a = complex(2, 3)
print(a)
# ---> (2+3j)


# 2 . To use complex number we can assign img part by suffix j
b = 3 + 4j
print(b)
# ---> (3+4j)


# 3. to access the real part
print(a.real)


# 4. to access imagnary part
print(a.imag)


# 5. conjugate of a complex num
conj_a = a.conjugate()
print(conj_a)


# 6. add complex num
sum = a+b
print(sum)


# 7.multiply complex num
prod = a*b
print(prod)


# 8.Division complex num
div = a/b
print(div)


# 9. for more comlex math
# import cmath
sqrt_of_neg = cmath.sqrt(-1)
print(sqrt_of_neg)
# ---> 1j

# 10. Python default math function do not produce complex number
# by default,
# import math
#sqrt_of_neg = math.sqrt(-1)
"""
Traceback(most recent call last):
  File "5-complex_number.py", line 53, in <module >
  sqrt_of_neg = math.sqrt(-1)
ValueError: math domain error
"""
