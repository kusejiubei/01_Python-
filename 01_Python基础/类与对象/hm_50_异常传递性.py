import logging


def demo1():
    in_str = int(input("请输入一个整数:"))
    print(in_str)


def demo2():
    demo1()


try:
    demo2()
except Exception as result:
    print("出错：",result)
    # 打印异常详细信息↓
    logging.exception(result)
else:
    print("哈哈没有异常")
finally:
    print("over")
