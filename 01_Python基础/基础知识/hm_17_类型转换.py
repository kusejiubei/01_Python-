# 元祖、列表互转
name_list = ["zhangsan", 18, "lisi"]
tuple_name = tuple(name_list)
print(type(name_list), type(tuple_name))
name_list2 = list(tuple_name)
print(type(name_list2))

# 数字类型互转
num_f = 18.7
num_str = str(num_f)
print(num_f, num_str, type(num_str))
num_f2 = float(num_str)
print(num_f2,num_str,type(num_f2))
num_int = 19
num_f3 = float(num_int)
print(num_int,num_f3,type(num_f3))
num_int2 = int(num_f3)
print(num_int2,num_f3,type(num_int2))
num_int3 = int(num_f)
print(num_int3,num_f,type(num_int3))
