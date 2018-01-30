#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:04

@author: Alan
'''
import myssqls
class UrlManager(object):
    def __init__(self):
        thedata=myssqls.DoSql()
        self.new_urls = thedata.selectNewUrl()
        self.old_urls = thedata.selectOldUrl()
    
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    
    def has_new_url(self):
        return len(self.new_urls) !=0
    
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def get_all_url(self):
        new_url = self.new_urls
        return new_url
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



