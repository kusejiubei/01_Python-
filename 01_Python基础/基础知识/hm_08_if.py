name = "张普"
age = 17
if age > 23:
    print("您的年龄太大了， %s" % name)
    print("您的年龄太大了第二行了， %s" % name)
elif age <= 18:
    print("您还未成年哦, %s" % name)
    print("您还未成年哦, 第二行了%s" % name)
else:
    print("刚刚好，bingo, %s" % name)
    print("刚刚好，bingo,第二行了 %s" % name)
age_str = input("请输入年龄:")
in_age = float(age_str)
if in_age > 12:
    #  三目运算符(score_python if score_python>score_java else score_python)
    #  三目运算符 bool and 1 or 2
    print("%s" % (in_age < 39) and "你好少年" or "你好叔叔")
    print("%s" % "你好少年" if in_age < 39 else "你好叔叔")

if 1 in (1, 2, 3, 4):
    print("%d 在列表中。" % 1)
if 1 in [1, 2, 3, 4]:
    print("%d 在列表中。" % 1)
