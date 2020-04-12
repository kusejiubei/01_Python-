str_sample = "hello world"
str_sample2 = ""
str_sample3 = "    "
str_sample4 = "\r\t\n"
# 判断空白字符
print(str_sample.isspace(), str_sample2.isspace(), str_sample3.isspace(),str_sample4.isspace())
str_number ="12"
str_number2 = "①①⑴1"
str_number3 = "一千万壹"
# 判断数字 isdecimal精确数字 《 isdigit数学数字 《 isnumeric包含汉子
print(str_number.isnumeric(),str_number.isdigit(),str_number.isdecimal())
print(str_number2.isnumeric(),str_number2.isdigit(),str_number2.isdecimal())
print(str_number3.isnumeric(),str_number3.isdigit(),str_number3.isdecimal())

