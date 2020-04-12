from 类与对象 import hm_52_模块1, hm_52_模块2 as mk2
from 类与对象.hm_52_模块1 import hello  # 这种导入可以直接使用模块中的函数
from 类与对象.hm_52_模块1 import demo  # 这种导入可以直接使用模块中的函数

hm_52_模块1.demo()
# 可以起个别名
mk2.demo()
hello()
demo()
