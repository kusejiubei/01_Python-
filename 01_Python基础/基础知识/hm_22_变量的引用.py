from 基础知识.hm_13_函数定义 import chage_point

a = 1
b = a
print(id(a))
print(id(1))
print(id(b))
b = 3
print(id(a), id(b))
s = [{"name":"zhang","age":"22"}]
print(s, id(s))
chage_point(s)
print(s, id(s))
