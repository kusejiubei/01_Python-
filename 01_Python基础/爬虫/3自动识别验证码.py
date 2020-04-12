import re
import urllib.request
import requests
from PIL import Image
from bs4 import BeautifulSoup
import time

from pytesseract import pytesseract


def get_image(fp):
    """
        获取图片
    :param file_name:
    :return:
    """
    img = Image.open(fp)
    # 打印当前图片的模式以及格式
    # print('未转化前的: ', img.mode, img.format)
    # 使用系统默认工具打开图片
    # img.show()
    # 将图片进行降噪处理, 通过二值化去掉后面的背景色并加深文字对比度
    # L灰度转换
    image = img.convert('L')
    image.show()
    pixels = image.load()
    # 【二值化】阀值：standard
    standard1, standard2 = (100, 160)
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard2:
                pixels[x, y] = 255
            elif pixels[x, y] > standard1:
                pixels[x, y] = 100
            else:
                pixels[x, y] = 0
    # image.show()
    image.save("D:\\data\\code_black.PNG")
    # 【描边】阀值：standard
    for x in range(image.width):
        for y in range(image.height):
            try:
                if x >= image.width or y >= image.height:
                    pixels[x, y] = 255
                elif pixels[x, y] < standard2 and pixels[x + 1, y] < standard2 and pixels[x, y + 1] < standard2:
                    # 原点有值、下方有值、右方有值 则保留
                    pass
                else:
                    pixels[x, y] = 255
            except:
                print("==>", x, y, image.width, image.height)
    # image.show()
    image.save("D:\\data\\code_scan.PNG")
    return image


def image_to_text(img):
    """
    如果出现找不到训练库的位置, 需要我们手动自动
    语法: tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
    :param img:
    :return:
    """
    testdata_dir_config = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
    # 去掉非法字符，只保留字母数字
    textCode = re.sub("\W", "", textCode)
    return textCode


if __name__ == '__main__':
    fp = open("D:\\data\\code.PNG", "rb")
    print("时间：".center(50, "*"))
    l = time.time()
    print(l)
    img = get_image(fp)
    print(time.time() - l)
    text = image_to_text(img)
    print(time.time() - l)
    print("文本内容".center(50, "*"))
    print(text)
