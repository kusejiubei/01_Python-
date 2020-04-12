import urllib.parse

if __name__ == '__main__':
    financial_url = "http://11.push2his.eastmoney.com/api/qt/stock/kline/get"
    params = {'cb': '中文',
              'secid': '1.000001',
              'fields1': 'f1,f2,f3,f4,f5',
              'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58',
              'klt': '101',
              'fqt': '1',
              'end': '20500101',
              'lmt': '120',
              '_': '1582441122952'}
    encode_url = urllib.parse.urlencode(params, encoding="utf-8")
    print("encode_url:\n", encode_url)
    decode_url = urllib.parse.unquote(encode_url)
    decode_url = urllib.parse.unquote("/user/mobile/vold?link=http%3A%2F%2Fcrm2.qq.com%2Fpage%2Fportalpage%2Fwpa.php%3Fuin%3D4006999133%26cref%26ref%3D%26f%3D1%26ty%3D1%26ap%3D%26as%3D%26v%3D&pg=%E6%88%91%E7%9A%84%E8%B4%A6%E6%88%B7-%E9%87%91%E6%B1%87%E9%87%91%E8%9E%8D%E4%BA%92%E8%81%94%E7%BD%91%E9%87%91%E8%9E%8D%E5%B9%B3%E5%8F%B0&appid=&lt=link&pv_rf=https%3A%2F%2Fwww.jinhui365.com%2Fuser%2Fmobile%2Fvold&uuid=e09e3a7b-75f4-4716-adc0-3fa11703bf8b&pdf=1&qt=0&realp=0&wma=0&dir=0&fla=1&java=0&gears=0&ag=0&cookie=1&res=1280x1024&gt_ms=204")
    print("decode_url:\n", decode_url)
