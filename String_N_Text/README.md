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
