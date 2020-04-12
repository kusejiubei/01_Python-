str_sample = "hello world"
str_sample2 = '我的外号是"大帅哥"'
print(str_sample, str_sample2)
print("第六个字符是：", str_sample2[6], str_sample2[-1], str_sample2[1])
for char in str_sample2:
    print(char)
print(type(str_sample2))
print(len(str_sample2))
print(str_sample2.count('"'))
num_sample = 12
print(str_sample.isalnum())
# is类型的操作
str_1 = "W O Ai Ni 你"
print("{} {}".format(str_1, 2020))

str_2 = "我 \n H2 S爱你"
print(",".join(str_2.split()))
print(str_1.isalnum(), str_1.isupper(), str_1.istitle(), str_2.istitle(), "str".isidentifier(), str_1.isnumeric())
print("设置宽度并居中".center(50, "*"))
