def measure(temp=39):
    """
    默认参数
    :return:
    """
    print("测量开始")
    print("测量结束")
    # 返回元祖可以省略小括号
    return temp, 33


def measure2(num, *args, **kwargs):
    """
    多参数语法
    :param num: 接受一个参数
    :param args: 接受多个参数：可逗号隔开，
    :param kwargs: 接受多个键值： 可逗号隔开
    :return:
    """
    print(num)
    print(args)
    print(kwargs)


result = measure(333)
print(result)
gl_temp, gl_wetness = result  # 【自动拆包】
print(gl_temp, gl_wetness) # 【自动拆包打印】
gl_temp, gl_wetness = measure()
print(gl_temp, gl_wetness)
a = 12
b = 22
c = 33
print(a, b, c)
c, b, a = a, b, c   # 【自动封装、拆包】
print(a, b, c)
# 多值参数
measure2(99, 1, 2, 3, 4, 5, 6, name="xiaoming", age=19)
