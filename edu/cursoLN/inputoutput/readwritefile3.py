import json
'''
This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class i
nstances in JSON requires a bit of extra effort.
'''
# with open('fjson','a') as f:
#     json.dump([1, 'simple', 'list'],f)
# f.closed

with open('fjson','r') as f:
    x=json.load(f)
    print(x[1])
f.closed