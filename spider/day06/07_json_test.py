import json

item = {'name':"李寻欢", 'card':'小李飞刀'}
with open('xiaolizhi.json', 'w') as f:
    json.dump(item, f, ensure_ascii=False)


with open('xiaolizhi.json') as f:
    data = json.load(f)


print(type(data))


item_list = [
    {'name':'紫衫龙王', 'card':'123'},
    {'name':'青翼蝠王', 'card':'456'}
]
with open('yttlj.json', 'a') as f:
    json.dump(item_list, f, ensure_ascii=False)











