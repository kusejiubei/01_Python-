class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s吃" % self.name)

    def drink(self):
        print("%s喝" % self.name)

    def run(self):
        print("%s跑" % self.name)

    def sleep(self):
        print("%s睡" % self.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("姓名：%s  年龄 %d" % (self.name, self.age))

    def run(self):
        print("%s我站在跑步" % self.name)


class XiaoTianQuan(Person, Animal):
    """默认构造方法是第一个父类的有参构造方法， 第一个没有找第二个"""

    def fly(self):
        print("%s 会飞" % self.name)

    def drink(self):
        """ 多态：重写了父类drink的方法 """
        # super().drink()  # 3.x调用父类的方法
        # Dog.drink(self)  # 2.x调用父类的方法
        print("%s 喝的是雨露" % self.name)


def ask(animal):
    assert isinstance(animal, Animal)
    animal.drink()


print(XiaoTianQuan.__mro__)
xtq = XiaoTianQuan("哮天犬", 109)
xtq.run()  # 两个父类都有这个方法，那么会执行__mro__最先出现的方法
xtq.fly()
xtq.drink()
xtq.speak()
xtq.sleep()
ask(xtq)
