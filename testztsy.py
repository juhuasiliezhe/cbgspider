#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:42

@author: Alan
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import random
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

class HtmlGet(object):
    # def __init__(self):
        # dcap = dict(DesiredCapabilities.PHANTOMJS)
        # dcap["phantomjs.page.settings.userAgent"] = (
        #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        # )
        # # dcap["phantomjs.page.settings.loadImages"] = False
        # self.driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)



    def download(self):
        proxy = Proxy(
            {
                'proxyType': ProxyType.MANUAL,
                'httpProxy': '112.114.77.46:8118'  # 代理ip和端口
            }
        )
        # 新建一个“期望技能”，哈哈
        # desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
        # 把代理ip加入到技能中

        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        phont=set()
        phont.add('13500885484')
        phont.add('13500885344')
        phont.add('13500885235')
        phont.add('13500888665')
        phont.add('13500888758')
        phont.add('13500885456')
        proxy.add_to_capabilities(dcap)
        # driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)
        driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe',desired_capabilities=dcap)
        driver.get('https://login.zbj.com/register?fromurl=http%3A%2F%2Fwww.zbj.com%2F')
        # driver.get('http://www.zbfile.com/')
        time.sleep(2)
        driver.find_element_by_id("sacc").send_keys(random.choice(list(phont)))
        time.sleep(2)
        driver.find_element_by_xpath("//*[@class='btn-get-code  getCode']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@class='btn-get-code  getCode']").click()
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # content=soup.find_all("div", attrs={"class": "form-content"})
        # content = str(content).decode('unicode-escape')
        # print content
        # content=str(content).decode('unicode-escape')



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
        driver.close()
if __name__ == "__main__":
    # root_url = "http://www.ccgp.gov.cn/cggg/zygg/cjgg/index.htm"
    root_url = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=79&areaid=43&server_name=%C8%E7%D2%E2%B5%BA&page=1&kindid=27&kind_depth=2"
    obj_spider = HtmlGet()
    obj_spider.download()