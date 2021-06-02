import string


# 1. interpolate string using format method
message = '{name} has {n} messages...'
new_message = message.format(name='Avinash', n=20)
print(new_message)
# ---> Avinash has 20 messages...


# 2. interpolate string using format_map() and vars()
message = '{student} has unique id : {id}'
student = 'Avinash'
id = 9
new_message = message.format_map(vars())
print(new_message)
# ---> Avinash has unique id : 9


# 3 . define a class the pass the instance to vars()
class Info:
    def __init__(self, student, id):
        self.student = student
        self.id = id


a = Info('sam', 12)
new_message = message.format_map(vars(a))
print(new_message)
# ---> sam has unique id : 12


# 4. some interesting string interpolation
student = 'Avinash'
id = 41
s = string.Template('$student has $id messages.')
new_s = s.substitute(vars())
print(new_s)
# ---> Avinash has 41 messages.
