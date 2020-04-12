# 用到的库
import requests


# 用百度检测ip代理是否成功
url = 'https://www.jinhui365.com/?abc'

# 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.jinhui365.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
# 发送get请求
# response = requests.get(url=url, headers=headers, params=params,proxies=proxy)
session = requests.session()
response = None
for i in range(10):
    response = session.get(url=url, headers=headers)
    print("response".center(50, "*"))
    print(response.status_code)
# 获取返回页面保存到本地，便于查看
with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
