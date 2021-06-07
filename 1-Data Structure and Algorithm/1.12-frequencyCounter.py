from collections import Counter

#=======================#
# Frequency of elements #
#=======================#

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# return a dictionaries with word as key and cont as value
word_count = Counter(words)
print(word_count)
"""
Output:
Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
 'not': 1, "don't": 1, "you're": 1, 'under': 1})
"""

# top three most frequent words
top_three = word_count.most_common(3)
print(top_three)
"""
Output:
[('eyes', 8), ('the', 5), ('look', 4)]
"""
# update the word list
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in morewords:
    word_count[word] += 1

# or we can update like
word_count.update(morewords)
print(word_count)
"""
Output:
Counter({'eyes': 10, 'my': 5, 'the': 5, 'look': 4, 'into': 3, 'not': 3,
'around': 2, 'why': 2, 'are': 2, 'you': 2, 'looking': 2, 'in': 2,
"don't": 1, "you're": 1, 'under': 1})
"""
# pop wiill remove that word from word_count dictionaries
print(word_count.pop('why'))
# ---> 2
