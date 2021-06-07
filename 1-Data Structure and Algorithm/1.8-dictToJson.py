import json
from collections import OrderedDict

d = OrderedDict()
d['avi'] = 1
d['ravi'] = 12
d['kavi'] = 13
d['davi'] = 145

print(d)
#OrderedDict([('avi', 1), ('ravi', 12), ('kavi', 13), ('davi', 145)])


print(json.dumps(d))
#{"avi": 1, "ravi": 12, "kavi": 13, "davi": 145}
