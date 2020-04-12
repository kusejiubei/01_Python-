str_blank = "*" * 30


def add_card(list_card):
    """
    新增
    :return:
    """
    print(str_blank)
    str_name = input("请输入姓名：")
    str_sex = input("请输入性别：")
    str_age = input("请输入年龄：")
    str_mobile = input("请输入手机号：")
    assert isinstance(list_card, list)
    list_card.append({"name": str_name, "sex": str_sex, "age": str_age, "mobile": str_mobile})
    print("添加成功！")
    return list_card


def update_card(list_card):
    """
    修改
    :return:
    """
    print(str_blank)
    i = input("请输入要修改的名片编号：")
    while not i.isdecimal():
        i = input("您的输入不合法，请输入编号：")
    str_name = input("请输入姓名<回车不修改>：")
    str_sex = input("请输入性别<回车不修改>：")
    str_age = input("请输入年龄<回车不修改>：")
    str_mobile = input("请输入手机号<回车不修改>：")
    assert isinstance(list_card, list)
    dict_temp = list_card[int(i)]
    assert isinstance(dict_temp, dict)
    if str_name.strip() != "":
        dict_temp["name"] = str_name
    if str_sex.strip() != "":
        dict_temp["sex"] = str_sex
    if str_age.strip() != "":
        dict_temp["age"] = str_age
    if str_mobile.strip() != "":
        dict_temp["mobile"] = str_mobile
    list_card[int(i)] = dict_temp
    print("修改成功！ id = %s" % i)
    return list_card


def delete_card(list_card):
    """
    删除
    :param list_card:
    :return:
    """
    if len(list_card) == 0:
        print("未找到任何名片记录，请先添加")
    else:
        i = input("请输入要删除的编号：")
        while not i.isdecimal():
            i = input("您的输入不合法，请输入编号：")
        assert isinstance(list_card, list)
        list_card.pop(int(i)-1)
        print("删除成功！ id = %s" % i)


def find_card(list_card):
    """
       查询
       :return:
       """
    print(str_blank)
    if len(list_card) > 0:
        print("编号\t姓名\t性别\t年龄\t手机号")
        assert isinstance(list_card, list)
        i = 0
        for dict_temp in list_card:
            assert isinstance(dict_temp, dict)
            i += 1
            print(i, end="\t")
            print(dict_temp.get("name"), end="\t")
            print(dict_temp.get("sex"), end="\t")
            print(dict_temp.get("age"), end="\t")
            print(dict_temp.get("mobile"))
    else:
        print("未找到名片记录")
    print(str_blank)
