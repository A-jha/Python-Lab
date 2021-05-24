record = ('Avi', 'avi@gmail.com', '912-343-2122', '892-244-3212')

# general way of unpacking
name, email, phone_num1, phone_num2 = record
print("phn1: ", phone_num1, "\n", "Phn2: ", phone_num2)
# Or we can store similar items in a list
name, email, *phone_num = record
print("List of phn : ", phone_num)

#--------Head Tail In Stack-----#
stack = [1, 20, 10, 11, 23, 34]
head, *dody, tail = stack
print("Head of stack is : ", head, "\nTail of stack is : ", tail)
