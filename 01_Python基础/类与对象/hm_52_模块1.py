title = "模块1"


def demo():
    print("我是%s" % title)


def main():
    print("这是%s  的print" % title)
    print("%s 打印内置属性__name__: %s" % (title, __name__))


if __name__ == '__main__':
    # 只有本身是主函数才执行的测试代码
    main()
