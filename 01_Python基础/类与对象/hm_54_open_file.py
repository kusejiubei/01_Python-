# rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
# r     以读方式打开,文件必须存在，不存在则抛出异常
# w     以写方式打开，不存在则创建；存在则open清空内容
# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# x     以创建模式打开【不可读；不存在则创建，存在则报错】
# r+     以读写模式打开
# w+     以读写模式打开 (参见 w )
# a+     以读写模式打开 (参见 a )
# rb     以二进制读模式打开
# wb     以二进制写模式打开 (参见 w )
# ab     以二进制追加模式打开 (参见 a )
# rb+    以二进制读写模式打开 (参见 r+ )
# wb+    以二进制读写模式打开 (参见 w+ )
# ab+    以二进制读写模式打开 (参见 a+ )
"""
# 创建文件
fileHandle = open("test_file_demo.txt", "x", encoding="utf-8")
fileHandle.write("what are you doing")
fileHandle.flush()
fileHandle.close()
# 写文件
fileHandle = open("test_file_demo.txt", "a+", encoding="utf-8")
fileHandle.write("where are you ? ")
fileHandle.write("where are you ? ")
fileHandle.write("where are you ? \n")
fileHandle.write("where are you ? ")
list_1 = ["who are you ? ", "who are you ? ", "who are you ? "]
fileHandle.writelines(list_1)
# 读文件
fileHandle = open("test_file_demo.txt",mode="r", encoding="utf-8")
content = fileHandle.read()
print(content)
fileHandle.close()
# 以二进制读
fileHandle = open("test_file_demo.txt",mode="rb")
content = fileHandle.read()
print(content)
fileHandle.close()
# 读取n个字符
fileHandle = open("test_file_demo.txt",mode="r",encoding="utf-8")
content = fileHandle.read(4)
print(content)
content = fileHandle.read(4)
print(content)
fileHandle.close()
# readlines()将每一行形成一个元素, 放到一个列表中
fileHandle = open("test_file_demo.txt",mode="r",encoding="utf-8")
content = fileHandle.readlines()
fileHandle.close()
for line in content:
    print(line,end="")
else:
    print("<完>")
# 写入二进制,一个汉字=3个字节=3字符
fileHandle = open("test_file_demo.txt",mode="wb")
word = "金毛狮王"
fileHandle.write(word.encode("utf-8"))
fileHandle.flush()
# 移动光标
fileHandle = open("test_file_demo.txt", mode="r+", encoding="utf-8")
fileHandle.seek(0, 2) # 将光标移动到结尾
fileHandle.seek(2) # 将光标移动到第二个字符
print(fileHandle.tell()) # 目前处在第几个位置
print(fileHandle.read())
# 文件截断
fileHandle = open("test_file_demo.txt", mode="r+", encoding="utf-8")
print(fileHandle.tell())
fileHandle.truncate(23) # 如果给出了n. 则从开头n后进行截断, 如果不给n, 则从当前位置截断
print(fileHandle.tell())
"""
import os
#  文件修改:
#  ①将文件中的内容读取到内存中, 将信息修改完毕;
#  ②然后将源文件删除, 将新文件的名字改成老文件的名字.
f1 = open("test_file_demo.txt", mode="r", encoding="utf-8")
f2 = open("test_file_demo_new.txt", mode="w", encoding="utf-8")
for line in f1:
    print(line, end="")
    newLine = line.replace("马云", "马化腾")
    f2.write(newLine)
else:
    f2.close()
    f1.close()
    print("\n",f1.name, f2.name)
    os.remove(f1.name)
    os.rename(f2.name, f1.name)
