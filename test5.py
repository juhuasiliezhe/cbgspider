# coding=utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
driver = webdriver.Chrome(abspath)
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(7)
soup = BeautifulSoup(driver.page_source, 'lxml')

print soup.get_text()

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

ele_string = driver.find_element_by_xpath("//*[@id='1']/h3/a/em").text
if (ele_string == "Selenium"):
    print u"测试成功，结果和预期结果匹配！"

print(driver.capabilities['version'])

driver.find_element_by_xpath("//*[@id='s_tab']/a[text()='新闻']").click()  # 在搜索结果页面点击新闻类别

time.sleep(1)

print (driver.current_url)  # current_url 方法可以得到当前页面的URL 
print (driver.title)  # title方法可以获取当前页面的标题显示的字段 

driver.quit()