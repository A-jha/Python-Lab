#--------Output will be random after execution ------- #
import random
import math

#=================#
#     Random      #
#=================#

# Rnadom basic
random_floating_num = random.random()
print(random_floating_num)
# ---> 0.9406677561675867

# get an int between 0 to 10
print(math.floor(random_floating_num*10))
# ---> 9
# A lsit of choices
values = [1, 2, 3, 4, 5, 6]


# 1. random value from values
_rand = random.choice(values)
print(_rand)
# ---> Thios will print a random value from values


# 2.Random Sample

sample_of_2 = random.sample(values, 2)
print(sample_of_2)
# ---> Output: [4, 3]

sample_of_3 = random.sample(values, 3)
print(sample_of_3)
# ---> Output: [4, 2, 6]


# 3. Shuffle randomly #
print("original list items are ", values)
random.shuffle(values)
# ---> Output: original list items are[1, 2, 3, 4, 5, 6]

print("shuffled list items are ", values)
# ---> Output: shuffled list items are[4, 2, 6, 3, 1, 5]


#  4. Produce random integer array
randInt = []
for i in range(0, 10):
    randInt.append(random.randint(0, 10))

print(randInt)
# ---> [2, 5, 7, 2, 9, 2, 9, 6, 8, 1]


# sort array
randInt.sort()
print(randInt)
# ---> [1, 2, 2, 2, 5, 6, 7, 8, 9, 9]

# reverse array
randInt.reverse()
print(randInt)
# ---> [9, 9, 8, 7, 6, 5, 2, 2, 2, 1]


# length of array
print(randInt.__len__())
# ---> 10

# final result
print(randInt)
# ---> [9, 9, 8, 7, 6, 5, 2, 2, 2, 1]
