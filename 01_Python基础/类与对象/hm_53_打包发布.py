# 我们把hm_message 打包
"""


"""

from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="发送消息服务",  # 描述
      long_description="点对点ip，发送消息，接受消息",  # 详细描述
      author="pzhang",  # 作者
      author_email="pzhang@rxhui.com",  # 作者邮箱
      url="www.baidu.com",  # 主页
      platforms="21",
      license="apache.org",
      py_modules=["hm_message.send_message", "hm_message.receive_message"]  # 要打入的模块
      )

# 打包发布：首先构建模块如：setup.py 文件
# python3 setup.py build
# python3 setup.py sdist

# 把打好的包安装到系统环境中
# 解压缩： tar zxvf  hm_message-1.0.tar.gz
# 安装：python3 setup.py install

# 模块卸载
# import hm_message
# hm_message.__file__ 找到文件路径如：'C:\\Python34\\lib\\site-packages\\hm_message\\__init__.py'
# cd 到文件（site-packages）路径下 ，删除此文件即可：rm hm_message*
