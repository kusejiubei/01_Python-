class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        """
        new 方法，单例模式的依据
            1创建对象时，new方法自动被调用
            2为对象分配空间
            3返回对象的引用
        :param args:
        :param kwargs:
        :return:
        """
        if cls.instance is None:
            cls.instance = (super().__new__(cls))
        print("come:", id(cls.instance))
        return cls.instance

    def __init__(self, name):
        if not MusicPlayer.init_flag:
            self.name = name
            print("创建播放器,%s" % name)
            MusicPlayer.init_flag = True

    def __str__(self):
        return "对象:%s" % self.name


mp = MusicPlayer("等一分钟")
mp2 = MusicPlayer("痒")
print("=========以下指定输出：=========\n",id(mp), id(mp2))
print(mp, mp2)
