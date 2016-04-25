# !/usr/bin/python
# -*- coding:utf-8 -*-


"""
爬虫源代码 （用于爬取知乎图片）
作者：lvwenling
"""


import os
import requests
import warnings
from bs4 import BeautifulSoup



print u'…………………………………………………………………………………………………………'
print u'       …………………………… .知.乎.图.片.爬.虫. ……………………………'
print u'…………………………………………………………………………………………………………'


while(True):
    num = int(raw_input(u'\n1.请输入您需要爬取的网址:https://www.zhihu.com/question/'.encode('gbk')))
    url = 'https://www.zhihu.com/question/%d' % num

    address = raw_input(u'\n2.请输入保存路径(例:c:/picture/): '.encode('gbk'))
    if os.path.isdir(address):
        pass
    else:
        os.makedirs(address)


    def download_page(url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                          '537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'
        }
        data = requests.get(url, headers=headers, verify=False).content
        return data


    def cut_url(a):
        i = -1
        while a[i] != '.':
            i -= 1
        return a[i:]


    def get_html(html):
        name_num = 0
        print u'\n\n开始爬取网页 o(∩_∩)o…\n\n'

        soup = BeautifulSoup(html, "html.parser")

        for detail in soup.find_all('img'):
            image = detail.get('data-actualsrc')
            if image is None:
                pass
            else:
                name_num += 1
                pic = requests.get(image, verify=False)
                pic_name = str(name_num) + str(cut_url(image))
                print u'正在爬取第%d张图片, 图片地址：%s\n' % (name_num,image)
                with open(address + '\\' + pic_name, 'wb') as fp:
                    fp.write(pic.content)

        print u"\n爬取完成   共爬取%d张图片 ╰(￣▽￣)╭ \n " % name_num


    if __name__ == '__main__':

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            html = download_page(url)
            get_html(html)
            raw_input(u'按回车键继续\n'.encode('gbk'))
