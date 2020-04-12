import csv
import json
import urllib.parse
from io import StringIO

import requests
import xmltodict


def download(get_url):
    response = requests.get(get_url, timeout=3)
    if response.ok:
        with open("000001.txt", "wb+") as fr:
            fr.write(response.content)
            fr.flush()
            fr.close()
        # stringIo 可以让字符串转换为文件流，以使得操作更方便
        return StringIO(response.text)


def json2xml(json_txt):
    with open('000001.xml', 'w+',encoding="utf-8") as myfile:
        xml = ''
        try:
            xml = xmltodict.unparse(json_txt, encoding='utf-8')
        except:
            xml = xmltodict.unparse({'request': json_txt}, encoding='utf-8')
        finally:
            myfile.write(xml)
        myfile.flush()
        myfile.close()


def writer_in(mywriter, text, key):
    if type(text) == list:
        for item in text:
            assert isinstance(item, str)
            mywriter.writerow(item.split(","))
    elif type(text) == dict:
        mywriter.writerow([key])
        for k in text:
            writer_in(mywriter, text[k], k)
    else:
        mywriter.writerow([key, str(text) + "\t"])  # 保证是文本格式打印到excel中


def json2csv(json_txt):
    with open('000001.csv', 'w+') as myfile:
        mywriter = csv.writer(myfile)
        n = 0
        for key in json_txt:
            writer_in(mywriter, json_txt[key], key)


if __name__ == '__main__':
    shang_hai = "http://11.push2his.eastmoney.com/api/qt/stock/kline/get?&secid=1.000001&fields1=f1,f2,f3,f4,f5&fields2=f51,f52,f53,f54,f55,f56,f57,f58&klt=101&fqt=1&end=20500101&lmt=120&_=1582441122952";
    io_fr = download(shang_hai)
    json_txt = json.load(io_fr)
    print("stringIo解析".center(50, "*"))
    for key in json_txt:
        print(key, json_txt[key])

    print("文件解析".center(50, "*"))
    txt_fr = open("000001.txt", "r+", encoding="utf-8")
    json_txt = json.load(txt_fr)
    for key in json_txt:
        print(key, json_txt[key])
    json2xml(json_txt)
    json2csv(json_txt)
