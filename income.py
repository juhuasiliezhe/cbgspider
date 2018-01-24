# coding=utf-8

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path="D:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
#获取链接
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles =soup.find_all("a", attrs={"class": "soldImg"})
for index in range(len(titles)):
    print titles[index].get('href')





#点击下一页
driver.find_element_by_xpath("//*[@class='pages']/a[text()='下一页']").click()
