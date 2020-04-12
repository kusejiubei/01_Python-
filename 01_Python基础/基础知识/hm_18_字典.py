# 字典输出的顺序通常和定义的顺序是不一致的
xiao_ming = {"name":"xiaoming","age":18,"shengao":1.75}
print(xiao_ming.keys())
print(xiao_ming.values())
print(xiao_ming)
print(xiao_ming.get("name"))
print(xiao_ming["name"])
print(xiao_ming.setdefault("tizhong",44))
xiao_ming["name"]="xiaoqq"
xiao_ming["aihao"]="daziqiu"
print(xiao_ming)
xiao_ming.pop("name")
print(xiao_ming)
print(len(xiao_ming))
temp_dict = {"height":22,"age":99}
xiao_ming.update(temp_dict)
print(xiao_ming)
xiao_ming.clear()
print(xiao_ming)
print(type(xiao_ming))