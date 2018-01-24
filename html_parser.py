#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:29

@author: Alan
'''
import re
import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):


        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a',href=re.compile(r".htm$"))

        for link in links:
            new_url = link['href']

            new_full_url = urlparse.urljoin(page_url,new_url)
            print(unicode("新路径：", "utf-8")+new_full_url)
            new_urls.add(new_full_url)

        return new_urls
    
    
    def _get_new_data(self, page_url, soup):

        res_data = {}
        #url
        res_data["url"] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        
#         title_nade = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
#         res_data['title'] = title_nade.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        # contentDate = re.findall('class="vT_detail_main">(.*?)</div><script language="javascript" src="/images/detailAddon.js',soup, re.S)
        try:

            # driver = webdriver.PhantomJS()
            # driver.get(page_url)
            # contentDate = driver.find_element_by_class_name("vT_detail_content w760c").text

            # contentDate = re.findall('<div class="vT_detail_content w760c" style="display: block;">(.*?)</div>', soups)

            # contentDate = soup.find('div', class_="vT_detail_content w760c")
        # summary_node = soup.find('div',class_='vT_detail_nav_lks')

        # res_data['content'] = summary_node.text ()
            if 'index_'in page_url or 'index.htm' in page_url :
                res_data['content'] = unicode("1", "utf-8")
            else:
                aa = re.search('<body>(.*?)</body>',soup,re.S).group(1)
                res_data['content'] = aa.replace('div','p')


            # driver.quit()

        except:
            print('错误:没有对应内容数据')
            res_data['content'] = unicode("1", "utf-8")

        return res_data
        
    def parse(self,page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser")
        new_urls = self._get_new_urls(page_url,soup)

        # new_data = self._get_new_data(page_url,soup)
        new_data = self._get_new_data(page_url,html_cont)

        return new_urls,new_data
        
    



