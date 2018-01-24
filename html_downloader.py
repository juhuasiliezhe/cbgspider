#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:42

@author: Alan
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class HtmlDownloader(object):
    def __init__(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        )
        # dcap["phantomjs.page.settings.loadImages"] = False
        self.driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)
    def valueData(self,value,vlaue2):
        strinfo = re.compile('<[\s\S]*?>')
        b = strinfo.sub('', value)
        return str(b.replace(vlaue2,"").replace(" ",""))

    def download(self,url):
        if url is None:
            return None

        driver = self.driver
        driver.get(url)
        parserValue=HtmlDownloader()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content=soup.find_all("div", attrs={"class": "infoList goodsInfo"})
        content=str(content).decode('unicode-escape')


        # 编号
        matchObj = re.search(r'编号[\s\S]*?</li>',str(content), re.M | re.I)
        number=parserValue.valueData(matchObj.group(),"编号：")
        print "编号："+number

        # 卖家ID
        matchObj = re.search(r'名称[\s\S]*?</li>',str(content), re.M | re.I)
        sellerid = parserValue.valueData(matchObj.group(),"名称：")
        print "名称："+sellerid

        # 是否上架
        matchObj = re.search(r'是否上架[\s\S]*?</li>', str(content), re.M | re.I)
        puton = parserValue.valueData(matchObj.group(), "是否上架：")
        print "是否上架：" + puton

        # 区服
        servicediv = soup.find_all("div", attrs={"class": "userInfo cWhite"})
        servicedata = str(servicediv).decode('unicode-escape')
        matchObj = re.search(r'梦幻玩家[\s\S]*?</div>', str(servicedata), re.M | re.I)
        matchObj2 = re.search(r'<p>[\s\S]*?</p>', str(matchObj.group()), re.M | re.I)
        servicearea = parserValue.valueData(matchObj2.group(), "梦幻玩家")
        print "区服："+servicearea

        # 价格
        matchObj = re.search(r'价格[\s\S]*?（元）', str(content), re.M | re.I)
        price = parserValue.valueData(matchObj.group(), "价格：")
        print "价格："+price

        # 是否接受还价
        matchObj = re.search(r'是否接受还价[\s\S]*?</li>', str(content), re.M | re.I)
        haggle = parserValue.valueData(matchObj.group(), "是否接受还价：")
        print "是否接受还价：" + haggle
        # 出售剩余时间

        matchObj = re.search(r'"create_time" : "[\s\S]*?",', str(soup), re.M | re.I)
        saletime = matchObj.group().replace("create_time","")
        print "是出售剩余时间：" + str(saletime).replace(",","").replace("\"","").replace(" : ","")
        # 级别
        # level
        # 角色类型
        # roletype
        # 名称
        # rolename
        # 人气
        # lifes
        # 帮派
        # faction
        # 帮贡
        # factionoffer
        # 门派
        # school
        # 门贡
        # schooloffer
        # 气血
        # blood
        # 体质
        # physique
        # 魔法
        # magic
        # 魔力
        # magicpower
        # 命中
        # hit
        # 力量
        # power
        # 伤害
        # hurt
        # 耐力
        # endurance
        # 防御
        # defense
        # 敏捷
        # agile
        # 速度
        # speed
        # 潜力
        # potential
        # 法伤
        # spell
        # 靓号特效
        # goodnumber
        # 法防
        # defend
        # 成就点数
        # achievement
        # 获得经验
        # experience
        # 已用潜能果数量
        # potentialnum
        # 新版乾元丹数量
        # neweditionnum
        # 总经验
        # sumexperience
        # 月饼粽子食用量
        # mooncake
        # 原始种族
        # original
        # 已获得机缘属性
        # opportunity
        # 飞升 / 渡劫 / 化圣
        # soaring
        # 历史门派
        # history
        # 属性保存方案
        # retain
        # 攻击修炼
        # hurtcultivation
        # 防御修炼
        # defenscultivation
        # 法术修炼
        # magiccultivation
        # 抗法修炼
        # resistspell
        # 猎术修炼
        # hunting
        # 攻击控制力
        # hurtcon
        # 防御控制力
        # defensecon
        # 法术控制力
        # spellcon
        # 抗法控制力
        # resistspellcon
        # 婚否
        # marriage
        # 同袍
        # brother
        # 房屋
        # house
        # 牧场
        # pasture
        # 庭院
        # courtyard
        # 社区
        # community
        # 比武积分
        # tournament
        # 剑会积分
        # sword
        # 三界功绩
        # threeachievement

        role_basic = soup.find_all("table", attrs={"id": "role_basic"})

        # fout = open('output.html', 'w')
        # fout.write(str(soup))
        #
        # driver.find_element_by_id("role_skill").click()
        # time.sleep(1)
        # soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        # fout = open('output1.html', 'w')
        # fout.write(str(soup1))
        # return  html.text










