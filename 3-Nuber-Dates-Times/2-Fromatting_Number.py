
x = 1234.56789


# 1. two decimal places of accuracy
acc_2 = format(x, '0.2f')
print(acc_2)
# ---> 1234.57


# 2. Right Justified in 10 chars, one digit accuracy
right_x = format(x, '>10.1f')
print(right_x)
# --->       1234.6


# 3. Left Justified
left_x = format(x, '<10.1f')
print(left_x)
# --->1234.6


# 4. centered
centered_x = format(x, '^10.1f')
print(centered_x)
# --->   1234.6


# 5,inclusion of thousand saperator
thousand_sap_x = format(x, ',')
print(thousand_sap_x)
# ---> 1,234.56789


# 6. swap '.' with ','
swap_saperator = {ord('.'): ',', ord(','): '.'}
comma_sap_x = format(x, ',').translate(swap_saperator)
print(comma_sap_x)
# --->1.234, 56789
