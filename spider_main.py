#coding:utf-8
'''
Created on 2017-7-28

@author: DELL
'''
import url_manager
import html_downloader
import html_parser
import html_outputer
import datetime

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

        # self.page = 1
        # self.dirName = 'MMSpider'
        # # 这是一些配置 关闭loadimages可以加快速度 但是第二页的图片就不能获取了打开(默认)
        # cap = webdriver.DesiredCapabilities.PHANTOMJS
        # cap["phantomjs.page.settings.resourceTimeout"] = 1000
        # # cap["phantomjs.page.settings.loadImages"] = False
        # # cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        # self.driver = webdriver.PhantomJS(desired_capabilities=cap)

    def craw(self, root_url):
        now = datetime.datetime.now()
        print now.strftime('%Y-%m-%d %H:%M:%S')  
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                print html_cont
                new_urls, new_data = self.parser.parse(new_url,html_cont)

                self.urls.add_new_urls(new_urls)
                
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                # self.urls.add_new_url('http://www.ccgp.gov.cn/cggg/zygg/cjgg/index_%d.htm' % count)
                count = count + 1

            except:
                print 'craw failed'
                
        self.outputer.output_html()
        nows = datetime.datetime.now()
        print nows.strftime('%Y-%m-%d %H:%M:%S')  

if __name__=="__main__":
    # root_url = "http://www.ccgp.gov.cn/cggg/zygg/cjgg/index.htm"
    root_url = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=79&areaid=43&server_name=%C8%E7%D2%E2%B5%BA&page=1&kindid=27&kind_depth=2"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    