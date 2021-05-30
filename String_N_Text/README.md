# String And Text

## Splitting Strings on Any of Multiple Delimiters

- The split() method of string objects is really meant for very simple cases, and does not allow for multiple delimiters or account for possible whitespace around the delimiters.

- The re.split() function is useful because you can specify multiple patterns for the separator.

-

## Matching Text at the Start or End of a String

- A simple way to check the beginning or end of a string is to use the

  - str.startswith('http//')

  - str.endswith('.py') methods.

## Matching Strings Using Shell Wildcard Patterns

- wildcard patterns as are commonly used when working in Unix shells (e.g., _.py , Dat[0-9]_.csv , etc.).

- **fnmatch()**
  Test whether FILENAME matches PATTERN.

Patterns are Unix shell style: matches everything ? matches any single character [seq] matches any character in seq [!seq] matches any char not in seq An initial period in FILENAME is not special. Both FILENAME and PATTERN are first case-normalized if the operating system requires it. If you don't want this, use fnmatchcase(FILENAME, PATTERN).

Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system’s underlying filesystem (which varies based on operating system).

For example:

```Python
>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False
>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
>>>
```

- **fnmatchcase()**
  If this distinction matters, use fnmatchcase() instead. It matches exactly based on the lower- and uppercase conventions that you supply.

```python
>>> fnmatchcase('foo.txt', '*.TXT')
False
```

## Matching and Searching for Text Patterns

If the text you’re trying to match is a simple literal, you can often just use the basic string methods, such as str.find() , str.endswith() , str.startswith() , or similar.

```python
>>> text = 'yeah, but no, but yeah, but no, but yeah'
>>> # Exact match
>>> text == 'yeah'
False
>>> # Match at start or end
>>> text.startswith('yeah')
True
>>> text.endswith('no')
False
>>> # Search for the location of the first occurrence
>>> text.find('no')
10
```

For more complicated matching, use regular expressions and the re module. To illustrate the basic mechanics of using regular expressions, suppose you want to match dates specified as digits, such as “11/27/2012.”

```Python
>>> text1 = '11/27/2012'
>>> text2 = 'Nov 27, 2012'
>>> import re
>>> # Simple matching: \d+ means match one or more digits
>>>if re.match(r'\d+/\d+/\d+', text1):
... print('yes')
...else:
... print('no')
yes
>>>if re.match(r'\d+/\d+/\d+', text2):
... print('yes')
>>>else:
... print('no')
no

```

match() always tries to find the match at the start of a string. If you want to search text for all occurrences of a pattern, use the findall() method instead.

## Searching and Replacing Text

### str.replace() method

```python
text = 'yeah, but no, but yeah, but no, but yeah'
text1 = text.replace('yeah', 'yep')
```

### use regular expression

```python
import re
datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')
changed_pattern = datepattern.sub(r'\2-\3-\2', today)
print(changed_pattern)
#---> Output: today is 05-2021-05. my bday is 05-2021-05
```

## Searching and Replacing Case-Insensitive Text

```Python
text = 'UPPER PYTHON, lower python, Mixed Python'
search_python = re.findall('python', text, flags=re.IGNORECASE)
print(search_python)
# -->Output: ['PYTHON', 'python', 'Python']
```

## Stripping Unwanted Characters from Strings

The strip() method can be used to strip characters from the beginning or end of a string. lstrip() and rstrip() perform stripping from the left or right side, respectively.

```Python
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
```

## Sanitizing and Cleaning Up Text

Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page and you’d like to clean it up somehow.

```Python
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
```

## Aligning Text Strings

For basic alignment of strings, the ljust() , rjust() , and center() methods of strings can be used.

- **More detaile explanation go to 5-searching_and_replacing_text.py file**

```python
align_left = text.ljust(20, '-')
print(align_left)
# --> output: Hello Universe------
align_right = text.rjust(20, '*')
print(align_right)
# --> otput:******Hello Universe
align_center = text.center(20, '#')
print(align_center)
# --> Output: ###Hello Universe###
```

## Combining and Concatenating Strings
