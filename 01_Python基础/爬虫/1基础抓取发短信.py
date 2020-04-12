import urllib.request
import requests
from PIL import Image
from bs4 import BeautifulSoup
import time


def grab_text():
    """
    抓取网页源码
    :param url:
    :return:
    """
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.read().decode('utf-8'))


def grab_cookie():
    url_jh = "http://google.jinhui365.cn/login"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=C4C81FF316AAE4D95561586EDAF0F81A; userState=-1|0f6324b8ef69a31f1bcde68d8ae053d8*6jxNsEgBJ0cwQkCLscSRLAr1V_5PhN4nVZFcXgWLDSYEaodOORvk25q0h6V-MFmOWNpn7iuOyZSesSkFVVlELg==',
        'Host': 'google.jinhui365.cn',
        'Referer': 'http://google.jinhui365.cn/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    params = {'uinfo': '18515279796', 'password': '111111', 'loginType': '0'}
    response = requests.post(url_jh, headers=headers, data=params, allow_redirects=False)
    print("response.content:", response.content.decode('utf-8'))
    print("response.headers:", response.headers)
    print("cookies in request".center(50, "*"))
    for key, value in response.request._cookies.items():
        print('key = ', key + ' ||| value :' + value)
    print("cookies in response".center(50, "*"))
    for key, value in response.cookies.items():
        print('key = ', key + ' ||| value :' + value)
    # // 获取cookie后访问我的持仓
    personal = "http://google.jinhui365.cn/user/personalcenter"
    response2 = requests.get(personal, cookies=response.cookies, allow_redirects=False)
    print("response.content:", response2.content.decode('utf-8'))
    print("cookies in request".center(50, "*"))
    for key, value in response2.request._cookies.items():
        print('key = ', key + ' ||| value :' + value)
    print("cookies in response".center(50, "*"))
    for key, value in response2.cookies.items():
        print('key = ', key + ' ||| value :' + value)


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
    # 得到图片链接，
    f = open('D:/data/code.PNG', 'wb')
    f.write(r.content)
    f.flush()
    f.close()
    l_image = Image.open('D:/data/code.PNG')
    l_image.show("验证码")
    code = input('哥们.麻烦你输入验证码:')
    params['imgVcode'] = code
    print("session.cookies".center(50, "*"), '\n', session.cookies)
    # time.sleep(10)
    # print(session.params)
    # print(session.adapters)
    # print(session.headers)
    # print(session.max_redirects)
    r = session.post(mobile_url,params=params,timeout=10000)
    # headers.update(session.headers)
    # r = requests.post(mobile_url, params=params, cookies=session.cookies)
    print("r.content".center(50, "*"), '\n', r.status_code, r.content.decode('utf-8'))


if __name__ == '__main__':
    # grab_text()
    # grab_cookie()
    send_msg()
