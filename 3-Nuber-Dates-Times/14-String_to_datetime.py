from datetime import datetime

text = '2020-12-20'
y = datetime.strptime(text, '%y-%m-%d')
z = datetime.now()
diff = z-y
print(diff)
