prices = {
    'Apple': 80.89,
    'banana': 25.45,
    'grapes': 90.56,
    'mango': 89.56,
    'waterMillon': 10.65
}

# zip() - t is often useful to invert the keys and values of the dictionary
#  using zip() .
# ---Note the first argument in zip file is consideres as calculatable
# minimum price among the items
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

# maximum price
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# sorted prices
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(prices_sorted)
