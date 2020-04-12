#! C:\Python34>python.exe
from 名片管理系统.card_tools import *
import os
import json

list_main = []
if os.access("card.properties", os.R_OK):
    f1 = open("card.properties", "r", encoding="utf-8")
    str_file = f1.read()
    if len(str_file.strip()):
        list_main = json.loads(str_file)
    f1.close()
print("欢迎进入名片管理系统".center(50, "*"))
print("【1】：新增")
print("【2】：修改")
print("【3】：删除")
print("【4】：查询")
print("【0】：退出系统")
print("*" * 57)
while True:
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    try:
        if action_str == "1":
            add_card(list_main)
        elif action_str == "2":
            update_card(list_main)
        elif action_str == "3":
            delete_card(list_main)
        elif action_str == "4":
            find_card(list_main)
        elif action_str == "0":
            print("您已退出系统，再见")
            f = open("card.properties", "w", encoding="utf-8")
            f.write(json.dumps(list_main))
            f.flush()
            f.close()
            break
        else:
            print("操作错误 %s" % action_str)
            print("请输入序号：【1】新增【2】修改【3】删除【4】查询【0】退出系统")
    except:
        print("系统异常，请联系管理员！ 您将继续。。。")
