from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# return a dictionaries with word as key and cont as value
word_count = Counter(words)

# top three most frequent words
top_three = word_count.most_common(3)

# update the word list
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in morewords:
    word_count[word] += 1

# or we can update like
word_count.update(morewords)

# pop wiill remove that word from word_count dictionaries
print(word_count.pop('why'))
