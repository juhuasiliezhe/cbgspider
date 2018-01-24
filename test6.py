
#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#获取href
class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")

    def testEle(self):
        driver = self.driver
        driver.get('http://xyq.cbg.163.com/equip?s=79&eid=201801212300113-79-MCHMZPPRLOXEX')
        headers = {'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.8', 'Cache-Control': 'max-age=0', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36','Connection': 'keep-alive' ,'Referer':'http://www.baidu.com/'}

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        role_basic = soup.find_all("table", attrs={"id": "role_basic"})

        fout = open('output.html', 'w')
        fout.write(str(soup))

        driver.find_element_by_id("role_skill").click()
        time.sleep(1)
        soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        fout = open('output1.html', 'w')
        fout.write(str(soup1))










    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()

