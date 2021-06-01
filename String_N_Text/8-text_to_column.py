import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# 1. text wrap module
print(textwrap.fill(s, 70))
"""
Output:
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.
"""

print(textwrap.fill(s, 40))
"""
Output:
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under.
"""


# 2. Intial indent
print(textwrap.fill(s, 40, initial_indent='          '))
"""
Output:
          Look into my eyes, look into
my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around
the eyes, look into my eyes, you're
under.
"""


# 3. Subsequent indent
print(textwrap.fill(s, 40, subsequent_indent='     '))
"""
Output:
Look into my eyes, look into my eyes,
     the eyes, the eyes, the eyes, not
     around the eyes, don't look around
     the eyes, look into my eyes, you're
     under.
"""
