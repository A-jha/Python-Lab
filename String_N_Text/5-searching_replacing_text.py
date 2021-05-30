import re
# 1. For simple literal patterns,
text = 'yeah, but no, but yeah, but no, but yeah'

text1 = text.replace('yeah', 'yep')
print(text1)
# --->Output: yep, but no, but yep, but no, but yep


# 2.For more complicated patterns, use the sub()
#  functions/methods in the re module.
# if you want to convert 11/05/2021 to 2021-11-05

today = 'today is 11/05/2021. my bday is 21/05/2021'
changed_pattern = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', today)
print(changed_pattern)
# --->Output: today is 2021-11-05. my bday is 2021-21-05

"""
If you’re going to perform repeated substitutions of the same 
pattern, consider compiling it first for better performance.
"""

datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')
changed_pattern = datepattern.sub(r'\2-\3-\2', today)
print(changed_pattern)
# ---> Output: today is 05-2021-05. my bday is 05-2021-05


# 3.Case-Insensitive search and replace

text = 'UPPER PYTHON, lower python, Mixed Python'
search_python = re.findall('python', text, flags=re.IGNORECASE)
print(search_python)
# -->Output: ['PYTHON', 'python', 'Python']

repace_python_to_cobra = re.sub('python', 'cobra', text, flags=re.IGNORECASE)
print(repace_python_to_cobra)
# --> Output: UPPER cobra, lower cobra, Mixed cobra


# 4. some string functions
text = "Avinash"
print(text.upper())
# -->Output : AVINASH
print(text.lower())
# -->Output: avinash
print(text.capitalize())
# --> Output: Avinash


# 5. Unicode
s1 = 'Spicy gravy\u00f1o'
print(s1)
# -->Output: Spicy gravyño


# 6. striping unwanted charecters from string

# white space straping
s = '   hello universe      1\n'
print(s)
# --> Output:    hello universe      1
s_without_space = s.strip()
print(s_without_space)
# ---> Output: hello universe      1

s_without_left_space = s.lstrip()
print(s_without_left_space)
# ---> Output:hello universe      1
s_without_right_space = s.rstrip()
print(s_without_right_space)
# --->Output:   hello universe      1

# charecter striping
t = '----------hello--------universe========'
print(t)
# -->Output:----------hello--------universe == == == ==
strip_dash = t.strip('-')
print(strip_dash)
# -->Output:hello--------universe == == == ==
strip_equlas = t.strip('=')
print(strip_equlas)
# -->Output:----------hello--------universe
strip_dash_and_equals = t.strip('-=')
print(strip_dash_and_equals)
# -->Output:hello--------universe


# 7. cleaning up text

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
# -->Output:pýtĥöñ
#               is awesome

remap = {
    ord('\t'): " ",
    ord('\f'): " ",
    ord('\r'): None,  # deleted
    ord('\n'): " ",
}

a = s.translate(remap)
print(a)
# -->Output:pýtĥöñ is awesome


# 8 . Aligning text string
text = "Hello Universe"
align_left = text.ljust(20)
print(align_left)
# --> output: 'Hello Universe    '
align_right = text.rjust(20)
print(align_right)
# --> otput: '   Hello Universe'
align_center = text.center(20)
print(align_center)
# --> Output: '  Hello Universe  '


# 9. fill space
align_left = text.ljust(20, '-')
print(align_left)
# --> output: Hello Universe------
align_right = text.rjust(20, '*')
print(align_right)
# --> otput:******Hello Universe
align_center = text.center(20, '#')
print(align_center)
# --> Output: ###Hello Universe###


# 10. format function can also be used to easily align
align_right = format(text, '>20')
print(align_right)
# --> otput: '   Hello Universe'
align_left = format(text, '<20')
print(align_left)
# --> output: 'Hello Universe    '
align_center = format(text, '=^20')
print(align_center)
# --> Output: ===Hello Universe===


# 11.format function can be used with numbers too
x = 1.23456
align_right = format(x, '$>10')
print(align_right)
# -->output:$$$1.23456

# truncate the number
truncated_text = format(x, '*^10.2f')
print(truncated_text)
# -->Output: ***1.23***
