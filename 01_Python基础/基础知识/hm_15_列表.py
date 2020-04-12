from 基础知识 import hm_13_函数定义

list_sample = ["zhangsan", "lisi", "wangwu", 12]
list_sample_new = hm_13_函数定义.sum_2_num(list_sample, ["dd"])
print(list_sample, list_sample_new)
print("列表中的第一个值：%s， 列表的长度 %d" % (list_sample[0], len(list_sample)))
list_sample.append("lisi")
list_sample.insert(3, "lisi")
list_sample[0] = "lisi"
list_sample_new = list_sample_new + list_sample
list_sample.extend(list_sample)
print("包含了 %d 个李四。李四的位置： %d" % (list_sample.count("lisi"), list_sample.index("lisi", 2, len(list_sample))))
print("old= %s new= %s" % (list_sample, list_sample_new))
list_sample.pop(1)
list_sample.pop()
list_sample.remove("wangwu")
print("old= %s new= %s" % (list_sample, list_sample_new))
del list_sample[2]
print("old= %s new= %s" % (list_sample, list_sample_new))
list_sample.remove(12)
list_sample.sort(reverse=True)
print("old= %s new= %s" % (list_sample, list_sample_new))
print(type(list_sample))

