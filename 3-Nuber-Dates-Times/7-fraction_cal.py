from fractions import Fraction

# 1. Fraction module
a = Fraction(5, 4)
print(a)
# ---> 5/4

b = Fraction(4, 5)
print(b)
# ---> 4/5

# 2. Sum of two fraction
print(a+b)
# --->41/20


# 3. multiple two fraction
c = a*b
print(c)
# ---> 1

# 4. get numerator and denominator
print(c.numerator)
# ---> 1
print(c.denominator)
# ---> 1


# 5. converting fractin to float
print(float(a+b))
# ---> 2.05

# 6. Coverting float to fraction
x = 7.5
y = Fraction(*x.as_integer_ratio())
print(y)
# ---> 15/2
