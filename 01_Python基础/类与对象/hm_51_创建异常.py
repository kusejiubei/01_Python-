def input_password():
    """
    密码必须： 输入大于8， 小于18 ； 否则抛出异常
    """
    password = input("请输入密码：")
    if len(password) > 18 or len(password) < 8:
        ex = Exception("密码过长 %s" % password)
        raise ex
    print("您输入的密码： %s" % password)


input_password()
