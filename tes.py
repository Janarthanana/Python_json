import json

a_dict = {'new_key': 'new_value'}

with open('rt.json') as f:
    data = json.load(f)

data.update(a_dict)

with open('test.json', 'w') as f:
    json.dump(data, f)