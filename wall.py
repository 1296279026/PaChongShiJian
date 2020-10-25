########################################################
#        Program to Download Wallpapers from           #
#                  alpha.wallhaven.cc                  #
#                                                      #
#                 Author - Saurabh Bhan                #
#                                                      #
#                  Dated- 26 June 2016                 #
#                 Update - 11 June 2019                #
########################################################

import os
import getpass
import re
import requests
import tqdm
import time
import urllib
import json

os.makedirs('小明同学壁纸爬虫', exist_ok=True)
BASEURL = ""
cookies = dict()

global APIKEY
APIKEY = "TRNGOxdYhyYsogfKlhmtpkcOb6pozzVf"
print('欢迎使用此软件，软件完全免费\n' + '软件作者：小明同学\n' + '软件如果不会使用请联系\n' + 'QQ:1296279026')


def category():
    global BASEURL
    print('''
    ****************************************************************
                            壁纸类别

    1       -所有壁纸.
    2       -常规壁纸.
    3       -动漫壁纸.
    4       -真人壁纸.
    5       -常规+动漫.
    6       -常规+真人.

    ****************************************************************
    ''')
    ccode = input('请输入: ').lower()
    ctags = {'1': '111', '2': '010', '3': '100', '4': '001', '5': '110', '6': '101'}
    ctag = ctags[ccode]

    print('''
    ****************************************************************
                            壁纸尺度

    1       -正常尺度
    2       -大尺度
    3       -暴露尺度
    4       -正常和大尺度
    5       -大尺度和暴露尺度
    6       -正常和暴露尺度
    7       -所有尺度

    ****************************************************************
    ''')
    pcode = input('请输入: ')
    ptags = {'1': '100', '2': '010', '3': '001', '4': '110', '5': '101', '6': '011', '7': '111'}
    ptag = ptags[pcode]

    BASEURL = 'https://wallhaven.cc/api/v1/search?apikey=' + APIKEY + "&categories=" + \
              ctag + '&purity=' + ptag + '&page='


def latest():
    global BASEURL
    print('Downloading latest')
    topListRange = '1M'
    BASEURL = 'https://wallhaven.cc/api/v1/search?apikey=' + APIKEY + '&topRange=' + \
              topListRange + '&sorting=toplist&page='


def search():
    global BASEURL
    query = input('输入你的关键字: ')
    BASEURL = 'https://wallhaven.cc/api/v1/search?apikey=' + APIKEY + '&q=' + \
              urllib.parse.quote_plus(query) + '&page='


def downloadPage(pageId, totalImage):
    url = BASEURL + str(pageId)
    urlreq = requests.get(url, cookies=cookies)
    pagesImages = json.loads(urlreq.content);
    pageData = pagesImages["data"]

    for i in range(len(pageData)):
        currentImage = (((pageId - 1) * 24) + (i + 1))

        url = pageData[i]["path"]

        filename = os.path.basename(url)
        osPath = os.path.join('小明同学壁纸爬虫', filename)
        if not os.path.exists(osPath):
            imgreq = requests.get(url, cookies=cookies)
            if imgreq.status_code == 200:
                print("下载中 : %s - %s / %s" % (filename, currentImage, totalImage))
                with open(osPath, 'ab') as imageFile:
                    for chunk in imgreq.iter_content(1024):
                        imageFile.write(chunk)
            elif (imgreq.status_code != 403 and imgreq.status_code != 404):
                print("不能下载 %s - %s / %s" % (filename, currentImage, totalImage))
        else:
            print("%s already exist - %s / %s" % (filename, currentImage, totalImage))


def main():
    Choice = input('''根据自己需求输入:

    输入 "1" -按类别搜索
    输入 "2" -获取当天最新的
    输入 "3" -按自己关键字搜索

    请输入: ''').lower()
    while Choice not in ['1', '2', '3']:
        if Choice != None:
            print('没有这个选项！！！\n' + '请退出重进')
        choice = input('Enter choice: ')

    if Choice == '1':
        category()
    elif Choice == '2':
        latest()
    elif Choice == '3':
        search()

    pgid = int(input('一页是24张\n' + '你想下载几页: '))
    totalImageToDownload = str(24 * pgid)
    print('总共需要下载: ' + totalImageToDownload)
    print('下载中，请耐心等待')
    for j in range(1, pgid + 1):
        downloadPage(j, totalImageToDownload)


if __name__ == '__main__':
    main()

# 软件不得用于商业用途
# 测试