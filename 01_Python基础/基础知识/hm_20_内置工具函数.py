import time

# len
tuple_sample = ("zhang", "pu", 12)
print(len(tuple_sample))
list_sample = [12, 22, 33, 44, 11]
# /max/min
print(max(list_sample), min(list_sample))
# /del
del (list_sample[0])
print(list_sample)
dict_sample = {"name": 1, "age": 232, "sex": 22}
print(max(dict_sample), min(dict_sample))
print(dict_sample.values(), max(dict_sample.values()), min(dict_sample.values()))
# >  <
print((2, 2, 3) < (2, 3, 2))
print("a" > "A")
# 切片  列表、元祖、字符串都支持切片
tuple_a = ("zhang", "pu", "is", "good", "boy")
print(tuple_a[1::2])
print(dir(tuple_a))  # 查看所有对象内置方法
print(id(tuple_a))  # 查看 对象指向的地址
print(tuple.mro())  # 查看 对象方法搜索顺序， 指向某个方法搜索的顺序：对多继承查看指向顺序很有用

time.sleep(1)  # 休眠1秒
