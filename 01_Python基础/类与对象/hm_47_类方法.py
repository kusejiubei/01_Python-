class Tools:
    count = 0

    @classmethod
    def show_instance_count(cls):
        print(cls.is_json_array(""))
        return cls.count

    @staticmethod
    def is_json_array(str_json):
        print(Tools.count)
        assert isinstance(str_json, str)
        if str_json.startswith("{") and str_json.endswith("}"):
            return True
        else:
            return False

    def __init__(self, name):
        Tools.count += 1
        self.name = name

    def __str__(self):
        return "工具%s" % self.name


# 类属性
jd = Tools("剪刀")
ft = Tools("斧头")
print("现在创建了 %d 个工具" % Tools.count)
print("现在创建了 %d 个工具" % jd.count)
print("现在创建了 %d 个工具" % ft.count)
# 静态方法
json_str = "{}"
print(Tools.is_json_array(json_str))
# 类方法
print("现在创建了 %d 个工具" % Tools.show_instance_count())
