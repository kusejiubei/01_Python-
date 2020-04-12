class Gun:
    """ 枪类"""

    def __init__(self, model):
        self.model = model
        self.bullet = 0

    def add_bullet(self, num):
        if num < 1:
            print("子弹数量必须大于0")
        print("装载了%d颗子弹" % num)
        self.bullet += num

    def shoot(self):
        if self.bullet < 1:
            print("枪里没有子弹了！")
        self.bullet -= 1
        print("%s开始突突" % self.model )

    def __str__(self):
        return "%s 里还有 %d颗子弹" % (self.model, self.bullet)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("%s 新士兵还没有枪" % self.name)
            return
        print("%s开枪射击,冲啊" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()

    def __str__(self):
        return "%s 的枪 %s" % (self.name, self.gun.model)


ak47 = Gun("ak47")
ak47.shoot()
ak47.add_bullet(10)
xu = Soldier("许三多")
xu.gun = ak47
print(xu)
xu.fire()


