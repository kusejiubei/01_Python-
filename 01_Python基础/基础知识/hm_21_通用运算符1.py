# + 可以在：字符串、元祖、列表 都可以使用
str_1 = "hello,"
str_2 = "python."
print(str_1 + str_2)
list_1 = [2, 3, "4", 9, "4", 4]
print(list_1, list_1.remove("4"), list_1)
list_2 = [8, 9, 8]
print(list_1 + list_2)
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
print(tuple_1 + tuple_2)
# 拓展extend：+会生成一个新的列表，extend则拼接到调用者上
list_1.extend(list_2)
print(list_1)
list_1.append(11)
print(list_1)
# 拓展append： 一次加一个元素
list_1.append([1, 2])
print(list_1)
