# 1. posetive infinity
import math
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

# 6. inf will propagate in calculation
a = float('inf')
print(a+45)
# --->inf

print(a*10)
# --->inf

print(a/10)
# --->inf

print(a/a)
# --->nan

print(a+b)
# --->nan

# 7. nan will propagate in calculation too
