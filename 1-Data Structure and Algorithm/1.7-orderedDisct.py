from collections import OrderedDict

d = OrderedDict()

d['avi'] = 1
d['arp'] = 2
d['sam'] = 3
d['ravi'] = 4

for key in d:
    print(key, d[key])
"""
Output:
avi 1
arp 2
sam 3
ravi 4
"""
