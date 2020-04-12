class Animal:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def eat(self):
        print("%s吃" % self.name)

    def drink(self):
        print("%s喝" % self.name)

    def run(self):
        print("%s跑" % self.name)

    def sleep(self):
        print("%s睡" % self.name)


class Dog(Animal):

    def bark(self):
        print("%s 叫" % self.name)


class XiaoTianQuan(Dog):
    def fly(self):
        print("%s 会飞" % self.name)

    def drink(self):
        """ 多态：重写了父类drink的方法 """
        # super().drink()  # 3.x调用父类的方法
        # Dog.drink(self)  # 2.x调用父类的方法
        print("%s 喝的是雨露" % self.name)


dog = Dog("小黄")
dog.run()
dog.drink()

xtq = XiaoTianQuan("哮天犬")
xtq.run()
xtq.fly()
xtq.drink()
