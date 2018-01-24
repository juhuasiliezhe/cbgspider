#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:42

@author: Alan
'''

import requests


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None


        hea = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
        # html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
        html = requests.get(url, headers=hea)

        html.encoding = 'GBK'
        status=html.status_code

        if status != 200:
            return None

        return  html.text









