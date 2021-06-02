
# 1.bin() function to convert decimal to binary string
d = 12
bin_d = bin(12)
print(bin_d)
# ---> 0b1100


# 2. oct() function is used to convert decimal to octal
oct_d = oct(d)
print(oct_d)
# ---> 0o14


# 3. hex() function is used to convert decimal to Hex
hex_d = hex(d)
print(hex_d)
# ---> 0xc


# 4. use format function to remove prefix 0b,0o,0x

# 4.1 d to b
bin_d = format(d, 'b')
print(bin_d)
# ---> 1100


# 4.2 d to o
oct_d = format(d, 'o')
print(oct_d)
# ---> 14


# 4.3 d to x
hex_d = format(d, 'x')
print(hex_d)
# ---> c


# 5. if number is negetive ouput will include -ve sign
neg_d = -12
bin_neg_d = bin(neg_d)
print(bin_neg_d)
# ---> -0b1100


# 6. To convert into integer from different bases

hex_no = 0xabcdef
int_no = int(hex_no)
print(int_no)
# ---> 11259375
