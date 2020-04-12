import os

# 查询目录
list_f = os.listdir(".")
for a in list_f:
    print(a)

# 创建目录
# os.mkdir("./temp", os.R_OK)
# 删除目录
# os.removedirs("./tmp")
# 重命名
# os.renames("./temp", "./tmp")
# 判断是否是一个文件或目录
# print(os.path.isdir("./tmp"), os.path.isfile("./tmp/新建 DOC 文档.doc"), os.path.isfile("./tmp/a.txt"))
# 获取当前位置目录
print("获取当前位置目录", os.getcwd())
# 执行系统命令
os.system("dir")
