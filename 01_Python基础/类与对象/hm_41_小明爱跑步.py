class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print("%s 爱跑步，跑步可以减肥。%s 的体重是 %.2f" % (self.name, self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("%s 爱吃东西，吃东西会长胖， %s 的体重是 %.2f" % (self.name, self.name, self.weight))

    def __str__(self):
        return "%s 的体重是%.2f" % (self.name, self.weight)


xiao_ming = Person("小明", 75.0)
print(xiao_ming)
xiao_ming.run()
xiao_ming.eat()
print(xiao_ming)
print("小美开始了".center(50,"*"))
xiao_mei = Person("小美", 45)
print(xiao_mei)
xiao_mei.eat()
xiao_mei.run()
print(xiao_mei)