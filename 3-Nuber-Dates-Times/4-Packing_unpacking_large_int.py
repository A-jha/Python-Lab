data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# 1. Length of data
length = len(data)
print(length)
# ---> 16


# 2. To interprete byte as an int use int.from_bytes()
# and specify the byte ordering
little = int.from_bytes(data, 'little')
print(little)
# ---> 69120565665751139577663547927094891008

big = int.from_bytes(data, 'big')
print(big)
# ---> 94522842520747284487117727783387188


# 3. To convert big number to byte string use
# int.to_bytes() method, specify num of bytes and byte order
x = 94522842520747284487117727783387188
big_byte_string = x.to_bytes(16, 'big')
print(big_byte_string)
# ---> b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
