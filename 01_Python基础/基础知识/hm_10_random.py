import random
you_side = input("欢迎参与游戏：1剪刀 2石头 3布 \n请输入：").strip()
computer_side = random.randint(1,3)
you_total = 0
computer_total = 0
if type(eval(you_side)) == int:
    you_side = int(you_side)
    if you_side == computer_side:
        print("哦，平局")
    elif (you_side == 1 and computer_side == 3) or (you_side == 2 and computer_side == 1) \
            or (you_side == 3 and computer_side == 2):
        print("恭喜，你赢了")
        you_total = you_total + 1
    elif you_side > 3:
        print("请按照规则输入哦！1/2/3")
    else:
        print("哟，你输了哦")
        computer_total = computer_total + 1
else:
    print("请输入数字哦！")
total = you_total + computer_total
total = (0 if total == 0 else (you_total * 100 / total))
print("您的得分： %d  , 电脑得分： %d ， 您的成功率 %.2f %%" % (you_total, computer_total, total))
