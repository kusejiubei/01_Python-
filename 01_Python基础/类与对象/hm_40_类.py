""" __方法名__ ：2个下划线开头2个下划线结尾的函数都是内置函数"""


class Person:

    def __init__(self, name=None):
        """ 对象创建时调用的方法 """
        self.name = name
        print("哈哈，初始化方法！")

    def __del__(self):
        """ 对象销毁时调用的方法（使用del xx 删除对象也是把对象销毁）"""
        print("呵呵，对象销毁了！")

    def __str__(self):
        print("打印了对象本身:~~~~~~~")
        return "我是 %s" % self.name

    def eat(self):
        print("%s 正在吃东西" % self.name)

    def run(self):
        print("%s 正在跑步" % self.name)


ming = Person("Tom")
# 可以对对象直接添加属性，只对该对象有效
# ming.age = "小美"
ming.eat()
ming.run()
print(id(None))
print(ming)
print(id(ming))
print("%x " % id(ming))
print("-"*50)