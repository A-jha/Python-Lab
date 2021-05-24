data = ["Avinash", 21, 90.1, (2000, 7, 26)]

# unpack the data
name, age, gpa, dob = data
print("Name :", name, "Age :", age)

# unpack date of the data
name, age, gpa, (year, mon, day) = data
print("Year of Birth : ", year, "gpa : ", gpa)
