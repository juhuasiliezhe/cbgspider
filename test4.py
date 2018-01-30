# coding=utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.maximize_window()
driver.implicitly_wait(6)

driver.get('http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=79&areaid=43&server_name=%C8%E7%D2%E2%B5%BA&page=1&kindid=27&kind_depth=2')
# driver.find_element_by_id("kind_a_36").click()
driver.find_element_by_xpath("//*[@class='pages']/a[text()='下一页']").click()

time.sleep(4)
soup = BeautifulSoup(driver.page_source, 'html.parser')

titles =soup.find_all("a", attrs={"class": "soldImg"})
print len(titles)
for index in range(len(titles)):
    print titles[index].get('href')

# fout = open('output.html','w')
# fout.write(str(soup))
# print soup.get_text()





driver.quit()