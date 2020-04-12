#  年龄判断
age = 40
if 0 < age < 1000:
    print("符合条件 %d" % age)
else:
    print("不符合条件 %s" % age)
score_python = 87
score_java = 90
if score_java > 100 or score_python > 60:
    #  三目运算符(score_python if score_python>score_java else score_python)
    #  三目运算符 bool and 1 or 2
    print("考试通过 %s" % (score_python if score_python > score_java else score_python))
    print("考试通过 %s" % (score_python > score_java and score_java or score_python))
else:
    print("考试不及格 %s %s" % (score_python, score_java))
# not
isEmploy = False
if not isEmploy:
    print("非公司员工，禁止入内")
# holiday Name elif
holiday = "情人节！"
if holiday == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday == "圣诞节":
    print("买苹果")
    print("吃大餐")
elif holiday == "生日":
    print("买礼物")
    print("买蛋糕")
else:
    print("每天都是节日呀")
# 嵌套if

if holiday != "情人节":
    if age < 30:
        print("你好小娘子")
    else:
        print("老娘们，%d了，过啥情人节" % age)
