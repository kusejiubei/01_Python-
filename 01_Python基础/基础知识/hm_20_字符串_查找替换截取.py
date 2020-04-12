str_sample = "hello world"
# 查找替换
print(str_sample.startswith("hell"))
print(str_sample.endswith("world"))
print(str_sample.rfind("l"), str_sample.find("l"))
print(str_sample.replace("world", "python"), str_sample)
str_char = "  hello world \t\n "
# 截取
print("str_char:", str_char.strip(), ",", str_char.rstrip(), ",", str_char.lstrip(), ",")
str_sub = "hello world hhh \t\r \n"
# 拆分链接
print(str_sub.split(" "), str_sub.split())
print(",".join(str_sub.split()))
str_sub2 = "helloworld"
# 切片
print(str_sub2[2:4], str_sub2[2:], str_sub2[:2], str_sub2[:-2],str_sub2[::2],str_sub2[1::2],str_sub2[-2::-1])
