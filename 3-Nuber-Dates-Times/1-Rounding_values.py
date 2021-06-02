#--------Rounding Numerical values --------#


# 1. Use round(value, ndigit)
import math
from decimal import localcontext
from decimal import Decimal
import decimal
num = 1.23456
round1 = round(num, 1)
print(round1)
# ---> 1.2

num1 = 1.27654
round2 = round(num1, 2)
print(round2)
# ---> 1.28


# 2. If round(value,-ve ndigit)

num = 1234567
tens_of_num = round(num, -1)
lacs_of_num = round(num, -5)
print("tens of num is ", tens_of_num)
print("lacs of num is ", lacs_of_num)
# Output
# tens of num is 1234570
# lacs of num is 1200000


# 3. Accurate Decimal calculation
a = 4.2
b = 2.1
print(a+b)
# ---> 6.300000000000001

print((a+b) == 6.3)
# ---> False


# 4.Decimal module to avoid condition like 3.
#from decimal import Decimal
# --we are passing number as string other wise it will do as 3
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
# ---> 6.3
print((a+b) == 6.3)
# ---> False
print((a+b) == Decimal('6.3'))
# ---> True


# 5. Localcontext
# from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)
# ---> 0.7647058823529411764705882353

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
# ---> 0.765

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)
# ---> 0.76470588235294117647058823529411764705882352941176


# 6. Sum and fsum
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# ---> 0.0

# here 1 is dissapeared in two large digit sum
# to be precise a new method is introduced in math
#import math

print(math.fsum(nums))
# ---> 1.0
