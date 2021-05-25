import json
from collections import OrderedDict

d = OrderedDict()
d['avi'] = 1
d['ravi'] = 12
d['kavi'] = 13
d['davi'] = 145
print(d)
print(json.dumps(d))
