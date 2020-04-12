def multiple_table():
    # 99乘法表
    row = 1
    while row < 10:
        col = 0
        while col < row:
            col += 1
            print("%d * %d = %d" % (col, row, col * row), end="\t")
        print()
        row += 1


def say_hello(name):
    """
    :parameter 输入： 姓名
    :return 功能： 对 xx 打招呼
    """
    print("你好，世界 ")
    print("hello %s" % name)


def sum_2_num(num1, num2):
    """对两个数字的求和

    :param num1: 数字A
    :param num2: 数字B
    :return:  返回A+B
    """
    return num1 + num2


def print_line(line_char, times):
    """打印分割线"""
    print(line_char * times)


def print_lines(line_char, times, row):
    """
    打印row 行的分割线

    :param line_char: 分割线使用的分隔符
    :param times: 每个分割线使用的分隔符重复的次数
    :param row: 分割线条数
    """
    while row > 0:
        print_line(line_char, times)
        row -= 1


def chage_point(temp):
    """
    检查变量引用
    :param temp:
    :return:
    """
    print("函数输入：", temp, id(temp))
    if type(temp) == list:
        assert isinstance(temp, list)
        temp.append("哈哈变化")
    elif type(temp) == str:
        temp = str(temp)
        temp.center(50, "*")
    elif type(temp) == tuple:
        del temp
    elif type(temp) == int:
        temp = 1
    elif type(temp) == dict:
        temp = dict(temp)
        temp["name"] = "9999"
    else:
        temp = "e!"
    print("函数输出：", temp, id(temp))


def line_conf():
    def line(x):
        if x == 1 :
            return "tom是1 hh java"
        return 2 * x + 1

    return line  # return a function object


my_line = line_conf()
print(my_line(1).title())

static_name = "黑马程序员"
