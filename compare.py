#coding=utf-8
#FileName : pic.py
#Author ; Lei
#Date : 2018/11/29

import re
import requests
import sys
import io
import os
import random

url = 'http://www.jandan.net/ooxx'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36',
#     'Cookie': '_ga = GA1.2.916013087.1543484582;_gid = GA1.2.1485563038.1543484582;_gat_gtag_UA_462921_3 = 1',
# 'Host': 'jandan.net'}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

html = requests.get(url, headers=header).text
print(html)
reg = r'src="(.*?\.gif)" alt'
imgre = re.compile(reg)
imglist = re.findall(imgre, html)
# list = re.findall(r'//.+\.jpg', html)
print(imglist)
print(os.name)
def get_pic(html):
    for addr in imglist:
        i = 1
        try:
            pics = requests.get(addr, timeout=10)
        except requests.exceptions.ConnectionError:
            print('当前地址出错')
            continue

        fq = open('C:\\Users\\I308865\\Pictures\\new' + (i + '.jpg'), 'wb')
        fq.write(pics.content)
        fq.close()

# if __name__ == '__main__':
#     get_pic(html)