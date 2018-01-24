import time

from selenium import webdriver

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
header_info = {
    'user-agent': UA,
}
chromedriver_path = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path)
url = 'https://www.duitang.com/search/?kw=文豪野犬&type=feed'


def test_2():
    driver.get(url=url)
    time.sleep(1)
    for i in range(10):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
    title = driver.title
    print('driver.title===%s' % title)
    content = driver.page_source
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    mbpho_list = driver.find_elements_by_class_name('mbpho')
    count = 1
    for mbp in mbpho_list:
        src = mbp.find_element_by_tag_name('img').get_attribute('src')
        print('当前是第%d页,,,%d张图片,地址是%s' % (1, count, src))
        count += 1
    page_sth = driver.find_element_by_class_name('woo-pager')
    page_total = 1
    if page_sth:
        a_list = page_sth.find_elements_by_tag_name('a')
        for a in a_list:
            page_str = a.text
            try:
                page = int(page_str)
                if page > page_total:
                    page_total = page
            except Exception as e:
                print(e)
    print('获取到的最大页数是==%d' % page_total)
    if page_total < 2:
        return
    for i in range(1, page_total):
        page_num = i + 1
        temp_url = 'https://www.duitang.com/search/?kw=%E6%96%87%E8%B1%AA%E9%87%8E%E7%8A%AC&type=feed#!s-p' + str(
            page_num)
        test_3(page_num, temp_url)


def test_3(page_num, url):
    driver.get(url=url)
    time.sleep(1)
    for i in range(10):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
    mbpho_list = driver.find_elements_by_class_name('mbpho')
    count = 1
    for mbp in mbpho_list:
        src = mbp.find_element_by_tag_name('img').get_attribute('src')
        print('当前是第%d页,,,%d张图片,地址是%s' % (page_num, count, src))
        count += 1


if __name__ == '__main__':
    test_2()