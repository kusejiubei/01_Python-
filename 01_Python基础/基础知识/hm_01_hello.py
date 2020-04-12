import os

print("你好 ， 中国")
help(os)  # 查询整个模块函数的帮助信息
print("dir(os)".center(50, "*"))
print(dir(os))  # 查询整个模块的所有函数
help(os.read)  # 查询某个函数的帮助信息
print(os.read.__doc__)  # 查询某个函数的文档信息
