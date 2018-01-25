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
        try:
            strinfo = re.compile('<[\s\S]*?>')
            b = strinfo.sub('', value)
            return str(b.replace(vlaue2,"").replace(" ",""))
        except:
            return ""
    def getTheData(self,rolr,reme,content):
        try:
            matchObj = re.search(r''+rolr+'', str(content), re.M | re.I)
            strinfo = re.compile('<[\s\S]*?>')
            b = strinfo.sub('', matchObj.group())
            return str(b.replace(reme, "").replace(" ", ""))
        except:
            return ""


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

        print "角色网址："+url
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
        level = parserValue.getTheData('级别[\s\S]*?</td>', "级别：", str(content))
        print "级别：" + level

        # 角色类型
        roletype = parserValue.getTheData('角色[\s\S]*?</td>', "角色：", str(content))
        print "角色类型：" + roletype

        # 名称
        rolename = parserValue.getTheData('<td><strong>名称[\s\S]*?</td>', "名称：", str(content))
        print "名称：" + rolename

        # 人气
        lifes = parserValue.getTheData('人气[\s\S]*?</td>', "人气：", str(content))
        print "人气：" + lifes

        # 帮派
        faction=parserValue.getTheData('帮派[\s\S]*?</td>',"帮派：",str(content))
        print "帮派：" + faction

        # 帮贡
        factionoffer = parserValue.getTheData('帮贡[\s\S]*?</td>', "帮贡：", str(content))
        print "帮贡：" + factionoffer

        # 门派
        school = parserValue.getTheData('门派[\s\S]*?</td>', "门派：", str(content))
        print "门派：" + school

        # 门贡
        schooloffer = parserValue.getTheData('门贡[\s\S]*?</td>', "门贡：", str(content))
        print "门贡：" + schooloffer

        # 气血
        blood = parserValue.getTheData('气血[\s\S]*?</td>', "气血：", str(content))
        print "气血：" + blood

        # 体质
        physique = parserValue.getTheData('体质[\s\S]*?</td>', "体质：", str(content))
        print "体质：" + physique

        # 魔法
        magic = parserValue.getTheData('魔法[\s\S]*?</td>', "魔法：", str(content))
        print "魔法：" + magic

        # 魔力
        magicpower = parserValue.getTheData('魔力[\s\S]*?</td>', "魔力：", str(content))
        print "魔法：" + magicpower

        # 命中
        # hit
        hit = parserValue.getTheData('命中[\s\S]*?</td>', "命中：", str(content))
        print "命中：" + hit

        # 力量
        # power
        power = parserValue.getTheData('力量[\s\S]*?</td>', "力量：", str(content))
        print "力量：" + power

        # 伤害
        # hurt
        hurt = parserValue.getTheData('伤害[\s\S]*?</td>', "伤害：", str(content))
        print "伤害：" + hurt

        # 耐力
        # endurance
        endurance = parserValue.getTheData('耐力[\s\S]*?</td>', "耐力：", str(content))
        print "耐力：" + endurance

        # 防御
        # defense
        defense = parserValue.getTheData('防御[\s\S]*?</td>', "防御：", str(content))
        print "防御：" + defense


        # 敏捷
        agile = parserValue.getTheData('敏捷[\s\S]*?</td>', "敏捷：", str(content))
        print "敏捷：" + agile

        # 速度
        # speed
        speed = parserValue.getTheData('速度[\s\S]*?</td>', "速度：", str(content))
        print "速度：" + speed

        # 潜力
        # potential
        potential = parserValue.getTheData('潜力[\s\S]*?</td>', "潜力：", str(content))
        print "潜力：" + potential

        # 法伤
        # spell
        spell = parserValue.getTheData('法伤[\s\S]*?</td>', "法伤：", str(content))
        print "法伤：" + spell

        # 靓号特效
        # goodnumber
        goodnumber = parserValue.getTheData('靓号特效[\s\S]*?</td>', "靓号特效：", str(content))
        print "靓号特效：" + goodnumber

        # 法防
        # defend
        defend = parserValue.getTheData('法防[\s\S]*?</td>', "法防：", str(content))
        print "法防：" + defend

        # 成就点数
        # achievement
        achievement = parserValue.getTheData('成就点数[\s\S]*?</td>', "成就点数：", str(content))
        print "成就点数：" + achievement

        # 获得经验
        # experience
        experience = parserValue.getTheData('获得经验[\s\S]*?</td>', "获得经验：", str(content))
        print "获得经验：" + experience

        # 已用潜能果数量
        # potentialnum
        potentialnum = parserValue.getTheData('已用潜能果数量[\s\S]*?</td>', "已用潜能果数量：", str(content))
        print "已用潜能果数量：" + potentialnum

        # 新版乾元丹数量
        # neweditionnum
        neweditionnum = parserValue.getTheData('新版乾元丹数量[\s\S]*?</td>', "新版乾元丹数量：", str(content))
        print "新版乾元丹数量：" + neweditionnum

        # 总经验
        # sumexperience
        sumexperience = parserValue.getTheData('总经验[\s\S]*?</td>', "总经验：", str(content))
        print "总经验：" + sumexperience

        # 月饼粽子食用量
        # mooncake
        mooncake = parserValue.getTheData('月饼粽子食用量[\s\S]*?</td>', "月饼粽子食用量：", str(content))
        print "月饼粽子食用量：" + mooncake

        # 原始种族
        # original
        original = parserValue.getTheData('原始种族[\s\S]*?</td>', "原始种族：", str(content))
        print "原始种族：" + original

        # 已获得机缘属性
        # opportunity
        opportunity = parserValue.getTheData('已获得机缘属性[\s\S]*?</td>', "已获得机缘属性：", str(content))
        print "已获得机缘属性：" + opportunity

        # 飞升 / 渡劫 / 化圣
        # soaring
        soaring = parserValue.getTheData('飞升/渡劫/化圣[\s\S]*?</td>', "飞升/渡劫/化圣：", str(content))
        print "飞升/渡劫/化圣：" + soaring

        # 历史门派
        # history
        history = parserValue.getTheData('历史门派[\s\S]*?</td>', "历史门派：", str(content))
        print "历史门派：" + history

        # 属性保存方案
        # retain
        retain = parserValue.getTheData('属性保存方案[\s\S]*?</td>', "属性保存方案：", str(content))
        print "属性保存方案：" + retain

        # 攻击修炼
        # hurtcultivation
        hurtcultivation = parserValue.getTheData('攻击修炼[\s\S]*?</td>', "攻击修炼：", str(content))
        print "攻击修炼：" + hurtcultivation

        # 防御修炼
        # defenscultivation
        defenscultivation = parserValue.getTheData('防御修炼[\s\S]*?</td>', "防御修炼：", str(content))
        print "防御修炼：" + defenscultivation

        # 法术修炼
        # magiccultivation
        magiccultivation = parserValue.getTheData('法术修炼[\s\S]*?</td>', "法术修炼：", str(content))
        print "法术修炼：" + magiccultivation

        # 抗法修炼
        # resistspell
        resistspell = parserValue.getTheData('抗法修炼[\s\S]*?</td>', "抗法修炼：", str(content))
        print "抗法修炼：" + resistspell

        # 猎术修炼
        # hunting
        hunting = parserValue.getTheData('猎术修炼[\s\S]*?</td>', "猎术修炼：", str(content))
        print "猎术修炼：" + hunting

        # 攻击控制力
        # hurtcon
        hurtcon = parserValue.getTheData('攻击控制力[\s\S]*?</td>', "攻击控制力：", str(content))
        print "攻击控制力：" + hurtcon

        # 防御控制力
        # defensecon
        defensecon = parserValue.getTheData('防御控制力[\s\S]*?</td>', "防御控制力：", str(content))
        print "防御控制力：" + defensecon

        # 法术控制力
        # spellcon
        spellcon = parserValue.getTheData('法术控制力[\s\S]*?</td>', "法术控制力：", str(content))
        print "法术控制力：" + spellcon

        # 抗法控制力
        # resistspellcon
        resistspellcon = parserValue.getTheData('抗法控制力[\s\S]*?</td>', "抗法控制力：", str(content))
        print "抗法控制力：" + resistspellcon

        # 婚否
        # marriage
        marriage = parserValue.getTheData('婚否[\s\S]*?</td>', "婚否：", str(content))
        print "婚否：" + marriage

        # 同袍
        # brother
        brother = parserValue.getTheData('同袍[\s\S]*?</td>', "同袍：", str(content))
        print "同袍：" + brother

        # 房屋
        # house
        house = parserValue.getTheData('房屋[\s\S]*?</td>', "房屋：", str(content))
        print "房屋：" + house

        # 牧场
        # pasture
        pasture = parserValue.getTheData('牧场[\s\S]*?</td>', "牧场：", str(content))
        print "牧场：" + pasture

        # 庭院
        # courtyard
        courtyard = parserValue.getTheData('庭院[\s\S]*?</td>', "庭院：", str(content))
        print "庭院：" + courtyard

        # 社区
        # community
        community = parserValue.getTheData('社区[\s\S]*?</td>', "社区：", str(content))
        print "社区：" + community

        # 比武积分
        # tournament
        defense = parserValue.getTheData('防御[\s\S]*?</td>', "防御：", str(content))
        print "防御：" + defense

        # 剑会积分

        # sword
        sword = parserValue.getTheData('剑会积分[\s\S]*?</td>', "剑会积分：", str(content))
        print "剑会积分：" + sword

        # 三界功绩
        # threeachievement
        threeachievement = parserValue.getTheData('三界功绩[\s\S]*?</td>', "三界功绩：", str(content))
        print "三界功绩：" + threeachievement

        # role_basic = soup.find_all("table", attrs={"id": "role_basic"})


        #####人物技能
        driver.find_element_by_id("role_skill").click()

        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.find_all("div", attrs={"id": "role_info_box"})
        content = str(content).decode('unicode-escape')

        print "###########人物生活技能######"
        # 强身术
        # buildhealth
        buildhealth = parserValue.getTheData('<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0201.gif" width="40"/>[\s\S]*?</p>', "", str(content))
        print "强身术：" + buildhealth

        # 冥想
        # meditation
        meditation = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0202.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "冥想：" + meditation


        # 暗器技巧
        # weapon
        weapon = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0203.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "暗器技巧：" + weapon

        # 打造技巧
        # makes
        makes = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0204.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "打造技巧：" + makes

        # 裁缝技巧
        # tailor
        tailor = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0205.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "裁缝技巧：" + tailor

        # 中药医理
        # medicine
        medicine = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0206.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "中药医理：" + medicine

        # 炼金术
        # alchemy
        alchemy = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0207.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "炼金术：" + alchemy

        # 烹饪技巧
        # cooking
        cooking = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0208.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "烹饪技巧：" + cooking

        # 追捕技巧
        # chase
        chase = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0209.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "追捕技巧：" + chase

        # 逃离技巧
        # escape
        escape = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0210.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "逃离技巧：" + escape

        # 养生之道
        # health
        health = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0211.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "养生之道：" + health

        # 健身术
        # bodybuilding
        bodybuilding = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0212.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "健身术：" + bodybuilding

        # 巧匠之术
        # carpenter
        carpenter = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0216.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "巧匠之术：" + carpenter

        # 熔炼技巧
        # melting
        melting = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0217.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "熔炼技巧：" + melting

        # 灵石技巧
        # stone
        stone = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0218.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "灵石技巧：" + stone

        # 强壮
        # strong
        strong = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0230.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "强壮：" + strong

        # 淬灵之术
        # soul
        soul = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0231.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "淬灵之术：" + soul

        # 神速
        # godspeed
        godspeed = parserValue.getTheData(
            '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0237.gif" width="40"/>[\s\S]*?</p>',
            "", str(content))
        print "神速：" + godspeed

        # 打造熟练度
        # makenum
        makenum = parserValue.getTheData('打造熟练度[\s\S]*?</td>',"打造熟练度：", str(content))
        print "打造熟练度：" + makenum

        # 裁缝熟练度
        # tailornum
        tailornum = parserValue.getTheData('裁缝熟练度[\s\S]*?</td>', "裁缝熟练度：", str(content))

        print "裁缝熟练度：" + tailornum

        #人物的装备
        driver.find_element_by_id("role_equips").click()

        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        contentUsing = soup.find_all("table", attrs={"id": "RoleUsingEquips"})
        contentUsing = str(contentUsing).decode('unicode-escape')
        print "###########人物装备######"
        parserValue.getEquipData(str(contentUsing))

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
    #获取装备信息
    def getEquipData(self, content):
        try:
            strinfo = re.findall('<img[\s\S]*?>',content)

            for value in strinfo:
                #判断是灵饰
                lingshi = re.search(r'【灵饰类型】', str(value), re.M | re.I)
                if lingshi:
                    print '这是灵饰：' + value
                else:
                    matchObj = re.search(r'【装备角色】[\s\S]*?\"', str(value), re.M | re.I)
                    #判断是武器
                    if matchObj:
                        if '，'in str(matchObj.group()):
                            print '这是武器：'+value
                        #判断是防具
                        else:
                            print '这是防具：' + value
                    else:
                        print '这是防具：' + value
            return ""
            # strinfo = re.compile('<[\s\S]*?>')
            # b = strinfo.sub('', matchObj.group())
            # return str(b.replace(reme, "").replace(" ", ""))
        except:
            return ""










