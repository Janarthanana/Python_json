import json

a_dict = {'new_key1': 'new_value2'}

with open('rt.json') as f:
    data = json.load(f)

data.update(a_dict)

##with open('test.json', 'w') as f:
##    json.dump(data, f)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
