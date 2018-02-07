#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os
import time
import url_manager
import html_downloader
import datetime

def __init__(self):
    ii=1
    pass

def worker(urls):
    print '子进程'+urls
    downloader = html_downloader.HtmlDownloader()
    downloader.download(urls)



if __name__ == '__main__':
    now = datetime.datetime.now()

    urls = url_manager.UrlManager()
    print len(urls.new_urls)
    pool = Pool(6)
    for url in urls.new_urls:
        print("---%s---" % url)
        pool.apply_async(worker, (url,))

    print("---start---")
    pool.close()  # 关闭进程池，相当于不能够再添加新任务了
    pool.join()
    print("---end---")
    nows = datetime.datetime.now()
    print '开始时间：' +now.strftime('%Y-%m-%d %H:%M:%S')
    print '结束时间：' + nows.strftime('%Y-%m-%d %H:%M:%S')





