import json
# 写入数据到文件
data_list = [{'name': '小白'}, {'name': '小黑'}]
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False)
# 从文件读取数据
with open('data2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)
