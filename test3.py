
#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#获取href
class seleniumTest(unittest.TestCase):
    def setUp(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        # dcap["phantomjs.page.settings.loadImages"] = False
        self.driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe', desired_capabilities=dcap)

    def testEle(self):
        driver = self.driver
        driver.get('http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=79&areaid=43&server_name=%C8%E7%D2%E2%B5%BA&page=1&kindid=27&kind_depth=2')
        headers = {'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.8', 'Cache-Control': 'max-age=0', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36','Connection': 'keep-alive' ,'Referer':'http://www.baidu.com/'}
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # titles = soup.find_all("table", attrs={"class": "soldList"})
        titles =soup.find_all("a", attrs={"class": "soldImg"})


        nums = soup.find_all('span', {'class': 'p1000'})
        print len(titles)
        for index in range(len(titles)):
            print titles[index].get('href')






    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()

