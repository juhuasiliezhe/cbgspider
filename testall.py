# coding:utf-8
'''
Created on 2017-7-28

@author: DELL
'''
import url_manager
import html_downloader
import datetime
import re


class SpiderMain2(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
    def craw(self, root_url):
        now = datetime.datetime.now()
        print '开始时间：' +now.strftime('%Y-%m-%d %H:%M:%S')

        try:
            # self.downloader.download('http://xyq.cbg.163.com/equip?s=221&eid=201801162000113-221-M5XS94ORRMBK')
            pass
        except ValueError, Argument:

            print 'craw failed', Argument

        nows = datetime.datetime.now()
        print '结束时间：' + nows.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    level = "0					"
    theneweditionnum = re.search(r'[0-9]+', level)
    print theneweditionnum.group()










































































