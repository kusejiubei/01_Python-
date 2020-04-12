from io import BytesIO

import urllib.request
import requests
from PIL import Image
from bs4 import BeautifulSoup
import time


def send_msg():
    mobile_url = "http://google.jinhui365.cn/vcode/mobile"
    img_url = "http://google.jinhui365.cn/kaptcha?action=kaptcha_register&32"
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Host': 'google.jinhui365.cn',
               'Origin': 'http://google.jinhui365.cn',
               'Referer': 'http://google.jinhui365.cn/register/index',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}
    params = {'mobile': '11120190203',
              'type': 'register',
              'is_web_a': '2020',
              'imgVcode': 'dhc8to',
              'isCheckDup': 'true',
              'isImgVcode': '1'}
    session = requests.Session()
    session.headers = headers
    r = session.get(url=img_url)
    print("cookies in response".center(50, "*"))
    for key, value in r.cookies.items():
        print('key = ', key + ' ||| value :' + value)

    # soup = BeautifulSoup(r.text, 'lxml')
    # 得到图片链接，把文件下载到本地
    # f = open('D:/data/code.PNG', 'wb')
    # f.write(r.content)
    # f.flush()
    # f.close()
    # l_image = Image.open('D:/data/code.PNG')
    l_image = Image.open(BytesIO(r.content))
    l_image.show("验证码")
    code = input('Gay.麻烦你输入验证码:')
    l_image.close()
    params['imgVcode'] = code
    print("session.cookies".center(50, "*"), '\n', session.cookies)
    # time.sleep(10)
    # print(session.params)
    # print(session.adapters)
    # print(session.headers)
    # print(session.max_redirects)
    r = session.post(mobile_url, params=params, timeout=10000)
    # headers.update(session.headers)
    # r = requests.post(mobile_url, params=params, cookies=session.cookies)
    print("r.content".center(50, "*"), '\n', r.status_code, r.content.decode('utf-8'))


if __name__ == '__main__':
    send_msg()
