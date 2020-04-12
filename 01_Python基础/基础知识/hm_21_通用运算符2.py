# * 可以在：字符串、元祖、列表 都可以使用
str_1 = "hello,"
print(str_1 * 2)
list_1 = [1, 2, 3]
print(list_1 * 2)
tuple_1 = (1, 2, 3)
print(tuple_1 * 2)

# in not in 可以对字符串、元祖、列表、字典 都可以使用
print("h" in str_1)
print(1 in list_1)
print(1 not in tuple_1)
dict_1 = {"name": "zhang", "age": 12}
print("name" in dict_1)
print("zhang" in dict_1)
