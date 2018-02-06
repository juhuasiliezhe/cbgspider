#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:42

@author: Alan
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import multiprocessing
import myssqls
import url_manager
import sys
import pymysql as MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')

class HtmlDownloaderGetUrl(object):
    def __init__(self):
        self.thesql = myssqls.DoSql()
        self.urls = url_manager.UrlManager()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        # dcap["phantomjs.page.settings.loadImages"] = False
        # self.driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)
        self.driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(6)
        # self.driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe',desired_capabilities=dcap)
    def download(self,url):
        if url is None:
            return None

        driver = self.driver

        driver.get('http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=221&areaid=14&server_name=%D1%A9%D3%F2%CC%EC%C1%FA&page=1&query_order=selling_time+DESC&kindid=27&kind_depth=2')
        time.sleep(2)
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # content=soup.find_all("div", attrs={"class": "infoList goodsInfo"})
        # content=str(content).decode('unicode-escape')


        soup = BeautifulSoup(driver.page_source, 'html.parser')
        titles = soup.find_all("a", attrs={"class": "soldImg"})
        getpages = soup.find_all("div", attrs={"class": "pages"})
        getpages=str(getpages).decode('unicode-escape')
        pages = re.findall(r'共[\s\S]*?页', str(getpages))
        allpage=pages[0].replace('共','').replace('页','')

        db = MySQLdb.connect()
        # 使用cursor()方法获取操作游标
        print int(allpage)
        print '第1页'
        for index in range(len(titles)):

            print titles[index].get('href')
            strd = titles[index].get('href')
            getmyurl = self.thesql.selectIfUrl('select  id from t_roleData where websiteid=\'' + strd + '\' ',db)

            if getmyurl==0:
                price = re.search(r'onmousedown=[\s\S]*?\)', str(titles[index]))
                theprice = price.group().replace(')', '').split(',')[1]
                sql = "INSERT INTO t_roleData(websiteid, \
                                                                       servicearea, issell, crawler,price) \
                                                                       VALUES ('%s',  '%s', '%s', '%d', '%.2f' )" % \
                      (titles[index].get('href'), '黑龙江区 雪域天龙', '否', 0, float(theprice))
                self.thesql.insertDataGetBig(sql,db)


        # 点击下一页
        # try:
        for page in range(int(allpage)-1):
            print '第'+str(page+2)+'页'
            driver.find_element_by_xpath("//*[@class='pages']/a[text()='下一页']").click()

            time.sleep(4)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            titles = soup.find_all("a", attrs={"class": "soldImg"})
            print len(titles)
            for index in range(len(titles)):
                print titles[index].get('href')
                strd=titles[index].get('href')
                getmyurl = self.thesql.selectIfUrl('select  id from t_roleData where websiteid=\'' + strd + '\' ',db)
                if getmyurl == 0:
                    price = re.search(r'onmousedown=[\s\S]*?\)', str(titles[index]))
                    theprice=price.group().replace(')', '').split(',')[1]
                    sql = "INSERT INTO t_roleData(websiteid, \
                                                       servicearea, issell, crawler,price) \
                                                       VALUES ('%s',  '%s', '%s', '%d', '%.2f' )" % \
                          (titles[index].get('href'), '黑龙江区 雪域天龙', '否', 0, float(theprice))
                    self.thesql.insertDataGetBig(sql, db)
        # except ValueError, Argument:
        #     print 'craw failed', Argument
        db.close()


        # time.sleep(1)



        # fout = open('output.html', 'w')
        # fout.write(str(soup))
        #
        # driver.find_element_by_id("role_skill").click()
        # time.sleep(1)
        # soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        # fout = open('output1.html', 'w')
        # fout.write(str(soup1))
        # return  html.text
        # driver.close()

if __name__ == "__main__":
    # root_url = "http://www.ccgp.gov.cn/cggg/zygg/cjgg/index.htm"
    obj_spider = HtmlDownloaderGetUrl()
    obj_spider.download('dfdfdf')




