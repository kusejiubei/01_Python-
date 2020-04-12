input_in = None
while True:
    try:
        input_in = int(input("请输入一个整数："))
        print("用户输入(8/in)是： %.2f" % (8 / input_in))
    except ZeroDivisionError:
        print("异常了呢！输入不能为0！")
    # except ValueError:
    #     print("抱歉，您输入的是字符串！")
    except Exception as result:  # 整体异常捕获
        print(result)  # 打印异常信息
    else:
        # 如果没有异常就会执行else
        print("执行了else")
    finally:
        # 不论有没有异常都会执行finally
        print("执行了finally")
