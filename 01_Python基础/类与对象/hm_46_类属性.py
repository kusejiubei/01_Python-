class Tools:
    count = 0

    def __init__(self, name):
        Tools.count += 1
        self.name = name
        self.count = 99

    def __str__(self):
        return "工具%s" % self.name


jd = Tools("剪刀")
ft = Tools("斧头")
print("现在创建了 %d 个工具" % Tools.count)
print("现在创建了 %d 个工具" % jd.count)
print("现在创建了 %d 个工具" % ft.count)
