class Women:
    def __init__(self, name):
        self.name = name
        """这是一个私有属性age"""
        self.__age = 16

    def set_age(self, age):
        self.__age = age

    def __secret(self):
        """ 这是一个私有方法"""
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def __str__(self):
        return "%s 的年龄是个秘密。" % self.name

    def speak(self):
        print("我叫%s, 我的年龄是%d" % (self.name, self.__age))


xiao_fang = Women("小芳")
xiao_fang.set_age(19)  # 通过共有方法设置私有属性
print(xiao_fang)
xiao_fang.speak()
""" 强制访问私有方法，真正开发是不建议使用的 """
print("强制访问私有方法/私有属性，真正开发是不建议使用的".center(50, "*"))
xiao_fang._Women__secret()
xiao_fang._Women__age = 18
xiao_fang.speak()

