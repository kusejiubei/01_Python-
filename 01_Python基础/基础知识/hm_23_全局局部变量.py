num = 22


def demo1():
    num = 10
    print("在demo1中内部变量是：", num)
    if True:
        a = 12
        print("if 条件内的变量：", a)
    print("if 条件外的变量：", a, num)
    for temp in (1, 2, 3):
        print("for内的变量：", temp)
    print("for 外的变量：", a, temp)


def demo2():
    global num  # global 关键字定义变量为全局变量中定义的变量
    num = 23
    print("在demo2中内部变量是：", num)


demo2()
demo1()
print("外层num :", num)
