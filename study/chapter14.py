import json

with open('study/json_example.json','r',encoding = 'utf8')as f:
    contents = f.read()
    json_data= json.loads(contents)
    print(json_data['employees'])

dict_data = {'Name':'Zara','Age':7,'Class':'First'}

with open('study/data.json','w') as f:
    json.dump(dict_data,f)