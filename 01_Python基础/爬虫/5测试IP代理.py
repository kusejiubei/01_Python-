# 用到的库
import requests

# 写入获取到的ip地址到proxy
proxy = {
    'https': '119.147.137.79:8008'
}
# 用百度检测ip代理是否成功
url = 'https://www.baidu.com/s?'
# 请求网页传的参数
params = {
    'word': 'ip地址'
}
# 请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.baidu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
# 发送get请求
# response = requests.get(url=url, headers=headers, params=params,proxies=proxy)
session = requests.session()
session.proxies = proxy
response = session.get(url=url, headers=headers, params=params)
print("response".center(50, "*"))
print(response.content.decode('utf-8'))
# 获取返回页面保存到本地，便于查看
with open('ip_baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
