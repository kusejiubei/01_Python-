from 类与对象 import hm_52_模块1, hm_52_模块2
import hm_message.send_message as msg  # 导入单个模块
import hm_message  # 导入模块包
from hm_message import *

title = "主模块"
print("打印导入的文件路径：")
print(hm_52_模块2.__file__)
print(hm_52_模块1.__file__)
# __name__ 在执行文件中永远都是：__main__，  导入的模块是对应文件名
print("%s 打印内置属性__name__: %s" % (title, __name__))

msg.send()
hm_message.receive_message.receive()
print("-" * 50)
send_message.send()
receive_message.receive()
