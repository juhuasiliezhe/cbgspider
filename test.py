# from selenium import webdriver
# driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
# driver.get("http://www.csdn.net")
# data = driver.title
# driver.save_screenshot('csdn.png')
#
# print(data)

#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")

    def testEle(self):
        driver = self.driver
        driver.get('http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=79&areaid=43&server_name=%C8%E7%D2%E2%B5%BA&page=1&kindid=27&kind_depth=2')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        titles = soup.find_all('td', {'class': 'soldImg'})
        nums = soup.find_all('span', {'class': 'p1000'})
        print len(titles)
        for index in range(len(titles)):
            print titles[index].get_text()
            # elem = driver.find_element_by_class_name('soldImg').click()
            # soup2 = BeautifulSoup(driver.page_source, 'html.parser')
            # print soup2.find_all('li', {'class': 'names'})



        # for title in titles:
        #     print title.get_text()
            # if driver.page_source.find('shark-pager-disable-next') != -1:
            #     break


    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()

