# for in else
for num in (1, 2, 3, 4):
    print(num)
else:
    # 只有in全部循环完毕才会执行else，如果for in 没有执行完 break退出了，就不会执行else
    print("会执行吗？")
print("循环结束")
students = [{"name": "阿图", "age": 19}, {"name": "jone", "age": 20}, {"name": "tom", "age": 12}]
find_name = "j"
for dictK in students:
    print(dictK)
    if dictK.get("name") == find_name:
        print("找到了 %s %s" % (find_name, dictK))
        break
else:
    print("没有找到 %s" % find_name)
