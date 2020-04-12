for i in range(3, 13, 3):  # 第一个是开始值(默认0)，第二个结束值，第三个是步长（默认为1）
    print(i)
for i in range(3):  # 第一个是开始值(默认0)，第二个结束值，第三个是步长（默认为1）
    print(i)
# 列表一般存储同种类型的数据
name_list = ["zhangsan", "lisi", "wangwu", 111]
for my_name in name_list:
    """
    数字类型包括： int float complex bool
    非数字类型： list列表[] tuple元祖()  dict字典{}  str字符串""/''
    所有非数字类型，都可以使用for循环
    """
    print("我的名字是： %s" % my_name)
# 元祖，打印的小括号本身就是元祖
tuple_sample = ("zhangsan", 18, 1.75)
for item in tuple_sample:
    print(item)
    if type(item) == str:
        print("是字符串数字吗？", item, item.isdigit())
print("姓名： %s, 年龄： %d, 身高： %.2f" % tuple_sample)
tuple_str = "tuple_str= 姓名： %s, 年龄： %d, 身高： %.2f" % tuple_sample
print(tuple_str)
print("看看内部变量可以打印吗？", my_name, item)
# 字典
dict_sample = {"name": "xiaoming", "age": 18, "height": 1.76}
for key in dict_sample:
    print(key, dict_sample[key])
