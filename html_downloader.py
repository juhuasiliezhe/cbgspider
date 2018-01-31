#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:24:42

@author: Alan
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import multiprocessing
import url_manager
import pymysql as MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class HtmlDownloader(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
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
        try:
            if url is None:
                return None

            driver = self.driver

            driver.get(url)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content=soup.find_all("div", attrs={"class": "infoList goodsInfo"})
            content=str(content).decode('unicode-escape')
            rolesAllDate={}
            print "角色网址："+url
            # 编号
            matchObj = re.search(r'编号[\s\S]*?</li>',str(content), re.M | re.I)
            number=self.valueData(matchObj.group(),"编号：")
            ###print "编号："+number
            rolesAllDate['number']=number

            # 卖家ID
            matchObj = re.search(r'名称[\s\S]*?</li>',str(content), re.M | re.I)
            sellerid = self.valueData(matchObj.group(),"名称：")
            ###print "名称："+sellerid
            rolesAllDate['sellerid'] = sellerid


            # 出售剩余时间
            matchObj = re.search(r'"create_time" : "[\s\S]*?",', str(soup), re.M | re.I)
            saletime = matchObj.group().replace("create_time","")
            ###print "是出售剩余时间：" + str(saletime).replace(",","").replace("\"","").replace(" : ","")

            rolesAllDate['saletime'] = str(saletime).replace(",","").replace("\"","").replace(" : ","")

            # 级别
            level = self.getTheData('级别[\s\S]*?</td>', "级别：", str(content))
            ###print "级别：" + level
            rolesAllDate['level']=int(level)

            # 角色类型
            roletype = self.getTheData('角色[\s\S]*?</td>', "角色：", str(content))
            ###print "角色类型：" + roletype
            rolesAllDate['roletype'] = roletype

            # 名称
            rolename = self.getTheData('<td><strong>名称[\s\S]*?</td>', "名称：", str(content))
            ###print "名称：" + rolename
            rolesAllDate['rolename'] = rolename

            # # 人气
            # lifes = self.getTheData('人气[\s\S]*?</td>', "人气：", str(content))
            # print "人气：" + lifes
            # rolesAllDate['lifes'] = lifes

            # # 帮派
            # faction=self.getTheData('帮派[\s\S]*?</td>',"帮派：",str(content))
            # print "帮派：" + faction
            # rolesAllDate['faction'] = faction

            # # 帮贡
            # factionoffer = self.getTheData('帮贡[\s\S]*?</td>', "帮贡：", str(content))
            # print "帮贡：" + factionoffer

            # 门派
            school = self.getTheData('门派[\s\S]*?</td>', "门派：", str(content))
            print "门派：" + school
            rolesAllDate['school'] = school

            # 门贡
            schooloffer = self.getTheData('门贡[\s\S]*?</td>', "门贡：", str(content))
            ###print "门贡：" + schooloffer
            rolesAllDate['schooloffer'] = int(schooloffer)

            # 气血
            blood = self.getTheData('气血[\s\S]*?</td>', "气血：", str(content))
            ###print "气血：" + blood
            rolesAllDate['blood'] = int(blood)


            # 体质
            physique = self.getTheData('体质[\s\S]*?</td>', "体质：", str(content))
            ###print "体质：" + physique
            rolesAllDate['physique'] = int(physique)

            # 魔法
            magic = self.getTheData('魔法[\s\S]*?</td>', "魔法：", str(content))
            ###print "魔法：" + magic
            rolesAllDate['magic'] =int(magic)

            # 魔力
            magicpower = self.getTheData('魔力[\s\S]*?</td>', "魔力：", str(content))
            ###print "魔力：" + magicpower
            rolesAllDate['magicpower'] = int(magicpower)


            # 命中
            # hit
            hit = self.getTheData('命中[\s\S]*?</td>', "命中：", str(content))
            ###print "命中：" + hit
            rolesAllDate['hit'] = int(hit)

            # 力量
            # power
            power = self.getTheData('力量[\s\S]*?</td>', "力量：", str(content))
            ###print "力量：" + power
            rolesAllDate['power'] = int(power)

            # 伤害
            # hurt
            hurt = self.getTheData('伤害：</strong>[\s\S]*?</td>', "伤害：", str(content))
            ###print "伤害：" + hurt
            rolesAllDate['hurt'] = int(hurt)

            # 耐力
            # endurance
            endurance = self.getTheData('耐力[\s\S]*?</td>', "耐力：", str(content))
            ###print "耐力：" + endurance
            rolesAllDate['endurance'] = int(endurance)

            # 防御
            # defense
            defense = self.getTheData('防御[\s\S]*?</td>', "防御：", str(content))
            ###print "防御：" + defense
            rolesAllDate['defense'] = int(defense)


            # 敏捷
            agile = self.getTheData('敏捷[\s\S]*?</td>', "敏捷：", str(content))
            ###print "敏捷：" + agile
            rolesAllDate['agile'] = int(agile)

            # 速度
            # speed
            speed = self.getTheData('速度[\s\S]*?</td>', "速度：", str(content))
            ###print "速度：" + speed
            rolesAllDate['speed'] = int(speed)

            # 潜力
            # potential
            potential = self.getTheData('潜力[\s\S]*?</td>', "潜力：", str(content))
            ###print "潜力：" + potential
            rolesAllDate['potential'] = int(potential)

            # 法伤
            # spell
            spell = self.getTheData('法伤[\s\S]*?</td>', "法伤：", str(content))
            ###print "法伤：" + spell
            rolesAllDate['spell'] = int(spell)

            # 靓号特效
            # goodnumber
            goodnumber = self.getTheData('靓号特效[\s\S]*?</td>', "靓号特效：", str(content))
            ###print "靓号特效：" + goodnumber
            rolesAllDate['goodnumber'] = goodnumber

            # 法防
            # defend
            defend = self.getTheData('法防[\s\S]*?</td>', "法防：", str(content))
            ###print "法防：" + defend
            rolesAllDate['defend'] = int(defend)

            # 成就点数
            # achievement
            achievement = self.getTheData('成就点数[\s\S]*?</td>', "成就点数：", str(content))
            ###print "成就点数：" + achievement
            rolesAllDate['achievement'] = int(achievement)

            # 获得经验
            # experience
            experience = self.getTheData('获得经验[\s\S]*?</td>', "获得经验：", str(content))
            ###print "获得经验：" + experience
            rolesAllDate['experience'] = experience

            # 已用潜能果数量
            # potentialnum
            potentialnum = self.getTheData('已用潜能果数量[\s\S]*?</td>', "已用潜能果数量：", str(content))
            ###print "已用潜能果数量：" + potentialnum
            rolesAllDate['potentialnum'] = int(potentialnum)

            # 新版乾元丹数量
            # neweditionnum
            neweditionnum = self.getTheData('新版乾元丹数量[\s\S]*?</td>', "新版乾元丹数量：", str(content))
            ###print "新版乾元丹数量：" + neweditionnum
            rolesAllDate['neweditionnum'] = int(neweditionnum)

            # 总经验
            # sumexperience
            sumexperience = self.getTheData('总经验[\s\S]*?</td>', "总经验：", str(content))
            ###print "总经验：" + sumexperience
            rolesAllDate['sumexperience'] = sumexperience

            # 月饼粽子食用量
            # mooncake
            mooncake = self.getTheData('月饼粽子食用量[\s\S]*?</td>', "月饼粽子食用量：", str(content))
            ###print "月饼粽子食用量：" + mooncake
            rolesAllDate['mooncake'] = int(mooncake)

            # 原始种族
            # original
            original = self.getTheData('原始种族[\s\S]*?</td>', "原始种族：", str(content))
            ###print "原始种族：" + original
            rolesAllDate['original'] = original

            # 已获得机缘属性
            # opportunity
            opportunity = self.getTheData('已获得机缘属性[\s\S]*?</td>', "已获得机缘属性：", str(content))
            ###print "已获得机缘属性：" + opportunity
            rolesAllDate['opportunity'] = opportunity

            # 飞升 / 渡劫 / 化圣
            # soaring
            soaring = self.getTheData('飞升/渡劫/化圣[\s\S]*?</td>', "飞升/渡劫/化圣：", str(content))
            ###print "飞升/渡劫/化圣：" + soaring
            rolesAllDate['soaring'] = soaring.replace('\t','')

            # 历史门派
            # history
            history = self.getTheData('历史门派[\s\S]*?</td>', "历史门派：", str(content))
            ###print "历史门派：" + history
            rolesAllDate['history'] = history

            # 属性保存方案
            # retain
            retain = self.getTheData('属性保存方案[\s\S]*?</td>', "属性保存方案：", str(content))
            ###print "属性保存方案：" + retain
            rolesAllDate['retain'] = retain

            # 攻击修炼
            # hurtcultivation
            hurtcultivation = self.getTheData('攻击修炼[\s\S]*?</td>', "攻击修炼：", str(content))
            ###print "攻击修炼：" + hurtcultivation.split('/')[0]
            rolesAllDate['hurtcultivation'] = int(hurtcultivation.split('/')[0])

            # 防御修炼
            # defenscultivation
            defenscultivation = self.getTheData('防御修炼[\s\S]*?</td>', "防御修炼：", str(content))
            ###print "防御修炼：" + defenscultivation
            rolesAllDate['defenscultivation'] = int(defenscultivation.split('/')[0])

            # 法术修炼
            # magiccultivation
            magiccultivation = self.getTheData('法术修炼[\s\S]*?</td>', "法术修炼：", str(content))
            ###print "法术修炼：" + magiccultivation
            rolesAllDate['magiccultivation'] = int(magiccultivation.split('/')[0])

            # 抗法修炼
            # resistspell
            resistspell = self.getTheData('抗法修炼[\s\S]*?</td>', "抗法修炼：", str(content))
            ###print "抗法修炼：" + resistspell
            rolesAllDate['resistspell'] = int(resistspell.split('/')[0])

            # 猎术修炼
            # hunting
            hunting = self.getTheData('猎术修炼[\s\S]*?</td>', "猎术修炼：", str(content))
            ###print "猎术修炼：" + hunting
            rolesAllDate['hunting'] = int(hunting)

            # 攻击控制力
            # hurtcon
            hurtcon = self.getTheData('攻击控制力[\s\S]*?</td>', "攻击控制力：", str(content))
            ###print "攻击控制力：" + hurtcon
            rolesAllDate['hurtcon'] = int(hurtcon)

            # 防御控制力
            # defensecon
            defensecon = self.getTheData('防御控制力[\s\S]*?</td>', "防御控制力：", str(content))
            ###print "防御控制力：" + defensecon
            rolesAllDate['defensecon'] = int(physique)

            # 法术控制力
            # spellcon
            spellcon = self.getTheData('法术控制力[\s\S]*?</td>', "法术控制力：", str(content))
            ###print "法术控制力：" + spellcon
            rolesAllDate['spellcon'] = int(spellcon)

            # 抗法控制力
            # resistspellcon
            resistspellcon = self.getTheData('抗法控制力[\s\S]*?</td>', "抗法控制力：", str(content))
            ###print "抗法控制力：" + resistspellcon
            rolesAllDate['resistspellcon'] = int(resistspellcon)

            # # 婚否
            # # marriage
            # marriage = self.getTheData('婚否[\s\S]*?</td>', "婚否：", str(content))
            # print "婚否：" + marriage
            # rolesAllDate['marriage'] = marriage

            # # 同袍
            # # brother
            # brother = self.getTheData('同袍[\s\S]*?</td>', "同袍：", str(content))
            # print "同袍：" + brother
            # rolesAllDate['brother'] = brother

            # # 房屋
            # # house
            # house = self.getTheData('房屋[\s\S]*?</td>', "房屋：", str(content))
            # print "房屋：" + house

            # # 牧场
            # # pasture
            # pasture = self.getTheData('牧场[\s\S]*?</td>', "牧场：", str(content))
            # print "牧场：" + pasture

            # # 庭院
            # # courtyard
            # courtyard = self.getTheData('庭院[\s\S]*?</td>', "庭院：", str(content))
            # print "庭院：" + courtyard

            # # 社区
            # # community
            # community = self.getTheData('社区[\s\S]*?</td>', "社区：", str(content))
            # print "社区：" + community

            # 比武积分
            # tournament
            defense = self.getTheData('防御[\s\S]*?</td>', "防御：", str(content))
            ###print "比武积分：" + defense
            rolesAllDate['defense'] = int(defense)

            # 剑会积分

            # sword
            sword = self.getTheData('剑会积分[\s\S]*?</td>', "剑会积分：", str(content))
            ###print "剑会积分：" + sword
            rolesAllDate['sword'] = int(sword)

            # 三界功绩
            # threeachievement
            threeachievement = self.getTheData('三界功绩[\s\S]*?</td>', "三界功绩：", str(content))
            ###print "三界功绩：" + threeachievement
            rolesAllDate['threeachievement'] = int(threeachievement)

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
            buildhealth = self.getTheData('<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0201.gif" width="40"/>[\s\S]*?</p>', "", str(content))
            ###print "强身术：" + buildhealth

            rolesAllDate['buildhealth'] = int(float(buildhealth+'.0'))

            # 冥想
            # meditation
            meditation = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0202.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "冥想：" + meditation
            rolesAllDate['meditation'] = int(float(meditation+'.0'))


            # 暗器技巧
            # weapon
            weapon = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0203.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "暗器技巧：" + weapon
            rolesAllDate['weapon'] = int(float(weapon+'.0'))

            # 打造技巧
            # makes
            makes = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0204.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "打造技巧：" + makes
            rolesAllDate['makes'] = int(float(makes+'.0'))


            # 裁缝技巧
            # tailor
            tailor = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0205.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "裁缝技巧：" + tailor
            rolesAllDate['tailor'] = int(float(tailor+'.0'))

            # 中药医理
            # medicine
            medicine = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0206.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "中药医理：" + medicine
            rolesAllDate['medicine'] = int(float(medicine+'.0'))

            # 炼金术
            # alchemy
            alchemy = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0207.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "炼金术：" + alchemy
            rolesAllDate['alchemy'] =int(float(alchemy+'.0'))

            # 烹饪技巧
            # cooking
            cooking = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0208.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "烹饪技巧：" + cooking
            rolesAllDate['cooking'] =int(float(cooking+'.0'))

            # 追捕技巧
            # chase
            chase = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0209.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "追捕技巧：" + chase
            rolesAllDate['chase'] = int(float(chase+'.0'))

            # 逃离技巧
            # escape
            escape = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0210.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "逃离技巧：" + escape
            rolesAllDate['escape'] =int(float(escape+'.0'))

            # 养生之道
            # health
            health = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0211.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "养生之道：" + health
            rolesAllDate['health'] =int(float(health+'.0'))

            # 健身术
            # bodybuilding
            bodybuilding = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0212.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "健身术：" + bodybuilding
            rolesAllDate['bodybuilding'] =int(float(bodybuilding+'.0'))

            # 巧匠之术
            # carpenter
            carpenter = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0216.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "巧匠之术：" + carpenter
            rolesAllDate['carpenter'] = int(float(carpenter+'.0'))

            # 熔炼技巧
            # melting
            melting = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0217.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "熔炼技巧：" + melting
            rolesAllDate['melting'] = int(float(melting+'.0'))

            # 灵石技巧
            # stone
            stone = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0218.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "灵石技巧：" + stone
            rolesAllDate['stone'] = int(float(stone+'.0'))

            # 强壮
            # strong
            strong = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0230.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "强壮：" + strong
            rolesAllDate['strong'] =  int(float(strong+'.0'))

            # 淬灵之术
            # soul
            soul = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0231.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "淬灵之术：" + soul
            rolesAllDate['soul'] = int(float(soul+'.0'))

            # 神速
            # godspeed
            godspeed = self.getTheData(
                '<img height="40" src="http://res.xyq.cbg.163.com/images/role_skills/0237.gif" width="40"/>[\s\S]*?</p>',
                "", str(content))
            ###print "神速：" + godspeed
            rolesAllDate['godspeed'] =int(float(godspeed+'.0'))

            # 打造熟练度
            # makenum
            makenum = self.getTheData('打造熟练度[\s\S]*?</td>',"打造熟练度：", str(content))
            ###print "打造熟练度：" + makenum
            rolesAllDate['makenum'] = int(float(makenum+'.0'))

            # 裁缝熟练度
            # tailornum
            tailornum = self.getTheData('裁缝熟练度[\s\S]*?</td>', "裁缝熟练度：", str(content))

            ###print "裁缝熟练度：" + tailornum
            rolesAllDate['tailornum'] = int(float(tailornum+'.0'))

            # sts =json.dumps(rolesAllDate, encoding="UTF-8", ensure_ascii=False).encode('unicode-escape').decode( 'string_escape')
            sts =json.dumps(rolesAllDate, encoding="UTF-8", ensure_ascii=False)
            print url
            thekey=sts.encode("utf-8").replace('\":','=').replace(', \"',',').replace("{\"",'').replace('\"}','').replace('}','')
            ###print '人物的属性数据：'+thekey

            # db = MySQLdb.connect(host='47.94.213.30', user='root', passwd='chenshixiao321', db='cbg', charset='utf8')

            # renwushuxingsql='update t_roleData set crawler=1 , '+renwushuxingsqlthekey+' where websiteid='+'\''+url+'\''
            renwushuxingsqlthekey=thekey
            # print renwushuxingsql
            # self.thesql.insertDataGetBig(renwushuxingsql, db)

            #人物的装备
            driver.find_element_by_id("role_equips").click()

            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            #身上的装备
            contentUsing = soup.find_all("table", attrs={"id": "RoleUsingEquips"})
            contentUsing = str(contentUsing).decode('unicode-escape')


            # 包裹中的装备
            contentHave = soup.find_all("table", attrs={"id": "RoleStoreEquips"})
            contentHave = str(contentHave).decode('unicode-escape')
            print "###########人物身上的装备######"
            self.getEquipData(str(contentUsing),url)
            print "###########人物包裹的装备######"
            self.getEquipData(str(contentHave),url)


            print "###########人物携带的宠物######"
            driver.find_element_by_id("role_pets").click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            thetest = re.findall(r'<td[\s\S]*?<img',str(soup.find_all("table", attrs={"id": "RolePets"})))
            print '宠物数量'+str(len(thetest))
            for val in range(len(thetest)):
                thesetValue={}
                driver.find_element_by_xpath("//*[@data_idx='"+str(val)+"']").click()
                time.sleep(1)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                contentpet = soup.find_all("table", attrs={"class": "tb02 petZiZhiTb"})
                contentpet = str(contentpet).decode('unicode-escape')
                #类型
                name = self.getTheData('类型[\s\S]*?</td>', "类型：", str(contentpet))
                thesetValue['name']=name

                # 等级
                level = self.getTheData('等级[\s\S]*?</td>', "等级：", str(contentpet))
                thesetValue['level'] = int(level)
                #技能
                petskill = soup.find_all("table", attrs={"class": "tb03"})
                skill = re.findall(r'/images/pet_child_skill[\s\S]*?.gif', str(petskill))
                thesetValue['skill'] =skill
                print val+1
                petsget= json.dumps(thesetValue, encoding="UTF-8", ensure_ascii=False).encode("utf-8")
                # print petsget.replace('\", \"',',').replace('\"], \"','').replace(': [','=').replace(': ','=')
                petsget2 = petsget.replace('{\"','').replace('[','').replace('\", \"/',',/').replace('], \"',',').replace('\":','=').replace('}','').replace('\", \"','\", ')

                print str('insert into t_petdata set websiteid=\''+url+'\', '+petsget2)
            print "###########人物携带的祥瑞######"
            # 祥瑞
            driver.find_element_by_id("role_riders").click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            getxiangrui = soup.find_all("table", attrs={"id": "RoleXiangRui"})
            getxiangrui=str(getxiangrui).decode('unicode-escape')
            putxiangrui = re.findall(r'<th[\s\S]*?</th>', str(getxiangrui))
            zuihou=''
            countNum=0
            for vd in putxiangrui:
                vd=vd.replace('<th>','').replace('</th>','')
                if countNum==1:
                    zuihou=vd
                elif countNum>1:
                    zuihou=zuihou+','+vd
                countNum+=1

            print "祥瑞reserveone：" + zuihou
            print "###########人物携带的坐骑######"

            thetest1 = re.findall(r'<td[\s\S]*?<img', str(soup.find_all("table", attrs={"id": "RoleRiders"})))
            print '坐骑数量' + str(len(thetest1))
            zuoqizong=''
            for val in range(len(thetest1)):
                driver.find_element_by_xpath("//*[@data_idx='" + str(val) + "']").click()
                time.sleep(1)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                contentRiders = soup.find_all("table", attrs={"class": "tb02"})
                contentRiders = str(contentRiders).decode('unicode-escape')
                contentRiderskill = soup.find_all("table", attrs={"class": "skillTb"})
                contentRiderskill = str(contentRiderskill).decode('unicode-escape')
                getdates = re.search(r'类型[\s\S]*?</td>', str(contentRiders))
                getskill = re.findall(r'rider_skill[\s\S]*?.gif', str(contentRiderskill))

                strinfo = re.compile('<[\s\S]*?>')
                b = strinfo.sub('',getdates.group())

                theallkill = ''
                for vals in range(len(getskill)):
                    theallkill += getskill[vals] + '*'

                zuoqizong+=zuoqizong+b+','+theallkill+';'

            print zuoqizong.replace('类型：','')

            print "###########人物携带的锦衣######"
            # 祥瑞
            driver.find_element_by_id("role_clothes").click()
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            getjingyi = soup.find_all("table", attrs={"id": "RoleClothesi"})
            getjingyi = str(getjingyi).decode('unicode-escape')
            putjingyi = re.findall(r'<th[\s\S]*?</th>', str(getjingyi))
            zuihou1 = ''
            countNum = 0


            for vd in putjingyi:
                vd = vd.replace('<th style="text-align:left">', '').replace('</th>', '')
                if countNum == 2:
                    zuihou = vd
                elif countNum > 2:
                    zuihou = zuihou + ',' + vd
                countNum += 1

            print "锦衣reservetwo：" + zuihou

            # db = MySQLdb.connect(host='47.94.213.30', user='root', passwd='chenshixiao321', db='cbg', charset='utf8')

            renwushuxingsql='update t_roleData set zuoji=\"'+zuoqizong.replace('类型：','')+'\",jinyi=\"'+zuihou+'\", crawler=1 , '+renwushuxingsqlthekey+' where websiteid='+'\''+url+'\''
            print renwushuxingsql
















            # # 身上的宠物
            # contentUsing = soup.find_all("table", attrs={"id": "RoleUsingEquips"})
            # contentUsing = str(contentUsing).decode('unicode-escape')



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
            # driver.close()
        except ValueError, Argument:
            print 'craw failed' ,Argument



    #获取装备信息
    def getEquipData(self, content,url):
        try:
            strinfo = re.findall('<img[\s\S]*?>',content)
            for value in strinfo:
                dictionary = {}#灵饰
                wuqiary = {}#武器
                fangjuary={}#防具
                #判断是灵饰
                lingshi = re.search(r'【灵饰类型】', str(value), re.M | re.I)
                # 名称
                name=self.getParserEquip('data_equip_name=\"[\s\S]*?\"',value)
                datas=self.getParserEquip('data_equip_desc=\"[\s\S]*?\"',value)
                getlever=self.getParserEquip('data_equip_type_desc=\"[\s\S]*?\"',value)
                whattype=''
                for thevalue in getlever.split("#r"):
                    if '【装备条件】等级' in thevalue:
                        dictionary['level'] = str(thevalue).replace("【装备条件】等级", '')
                    elif '【灵饰类型】' in thevalue:
                        dictionary['name'] = str(thevalue).replace("【灵饰类型】", '').replace('\"','')

                if lingshi:

                    for thekey in datas.split("#r"):

                        if '法术伤害'in thekey:
                            onevalue = '法术伤害'
                            twovalue = 'spell'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '耐久度'in thekey:
                            onevalue = '耐久度'
                            twovalue = 'durable'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '精炼等级'in thekey:
                            onevalue = '精炼等级'
                            twovalue = 'exercise'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '物理暴击等级'in thekey:
                            onevalue = '物理暴击等级'
                            twovalue = 'physicscrit'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '狂暴等级'in thekey:
                            onevalue = '狂暴等级'
                            twovalue = 'rage'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '固定伤害'in thekey:
                            onevalue = '固定伤害'
                            twovalue = 'fixed'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '伤害'in thekey:

                            onevalue = '伤害'
                            twovalue = 'hurt'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '穿刺等级 'in thekey:
                            onevalue = '穿刺等级'
                            twovalue = '穿刺puncture'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '速度'in thekey:
                            onevalue = '速度'
                            twovalue = 'speed'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '封印命中等级' in thekey:
                            onevalue = '封印命中等级'
                            twovalue = 'seal'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '防御' in thekey:
                            onevalue = '防御'
                            twovalue = 'defense'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '法术暴击等级' in thekey:
                            onevalue = '法术暴击等级'
                            twovalue = 'magiccrit'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '法术防御' in thekey:
                            onevalue = '法术防御'
                            twovalue = 'defend'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '气血' in thekey:
                            onevalue = '气血'
                            twovalue = 'blood'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '抵抗封印等级' in thekey:
                            onevalue = '抵抗封印等级'
                            twovalue = 'resistseal'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '格挡值' in thekey:
                            onevalue = '格挡值'
                            twovalue = 'block'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)
                        elif '气血回复效果' in thekey:
                            onevalue = '气血回复效果'
                            twovalue = 'reply'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)
                        elif '法术伤害' in thekey:
                            onevalue = '法术伤害'
                            twovalue = 'result'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)
                        elif '治疗能力' in thekey:
                            onevalue = '治疗能力'
                            twovalue = 'treatment'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)
                        elif '抗物理暴击等级' in thekey:
                            onevalue = '抗物理暴击等级'
                            twovalue = 'resistphysicscrit'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                        elif '抗法术暴击等级' in thekey:
                            onevalue='抗法术暴击等级'
                            twovalue='resistmagiccrit'
                            self.setDictData(onevalue, twovalue, thekey, dictionary)

                    print '这是灵饰【' + name+'】:' +json.dumps(dictionary, encoding="UTF-8", ensure_ascii=False)
                    whattype = 'insert into t_ornamentsdata set  websiteid=' + '\"' + url + '\",' + parserSql(dictionary)

                else:
                    matchObj = re.search(r'【装备角色】[\s\S]*?\"', str(value), re.M | re.I)
                    #判断是武器
                    if matchObj:
                        if '，'in str(matchObj.group()):
                            for thekey in datas.split("#r"):
                                if '五行' in thekey:
                                    thislevel= re.search(r'[0-9]+', str(value), re.M | re.I)
                                    wuqiary['level']=thislevel.group()
                                elif '命中' in thekey:
                                    minzhong = re.findall(r'[0-9]+', thekey)
                                    count = 0
                                    for val in minzhong:
                                        if count==0:
                                            wuqiary['hit'] = val
                                        else:
                                            wuqiary['hurt'] = val
                                        count+=1

                                elif '耐久度' in thekey:
                                    naijiu = re.findall(r'[0-9]+', thekey)
                                    count = 0
                                    datess=''
                                    for val in naijiu:
                                        if count==0:
                                            datess= val
                                        else:
                                            datess= datess+','+ val
                                        count+=1
                                    wuqiary['durable']=datess
                                elif '锻炼等级' in thekey:
                                    duanliandengji = re.search(r'[0-9]+', thekey)

                                    duanlianbaoshi = re.search(r'宝石[\s\S]*', thekey)
                                    wuqiary['exercise'] = duanliandengji.group()
                                    wuqiary['gemstone'] = duanlianbaoshi.group().replace('宝石 ','')
                                elif '#G#G' in thekey:
                                    fujia = re.findall(r'[^\u4e00-\u9fa5]+[0-9]+', thekey)

                                    count = 0
                                    for val in fujia:
                                        if count == 0:
                                            wuqiary['fujia'] = val
                                        else:
                                            wuqiary['fujia'] = wuqiary['fujia']+val
                                        count += 1

                                elif '特技' in thekey:
                                    teji = re.findall(r'[^\u4e00-\u9fa5^#]+', thekey)
                                    wuqiary['stunt'] = teji[1]
                                elif '特效' in thekey:
                                    texiao = re.findall(r'[^\u4e00-\u9fa5^#]+', thekey)

                                    wuqiary['effects'] = texiao[1]

                                elif '开运孔数' in thekey:
                                    kaikong = re.findall(r'[\u4e00-\u9fa5]+', thekey)
                                    wuqiary['holenum'] = kaikong[1]
                                elif '熔炼效果' in thekey:
                                    ronglian = re.findall(r'[+|-][0-9]+[^\u4e00-\u9fa5]* ', thekey)
                                    thrules = ''
                                    for num in range(len(ronglian)):
                                        if num == 0:
                                            thrules = ronglian[num]
                                        else:
                                            thrules = thrules + ',' + ronglian[num]

                                    wuqiary['melting'] = thrules

                                elif '套装效果' in thekey:
                                    taozhuang = re.findall(r'[^\u4e00-\u9fa5^#]+',thekey)
                                    wuqiary['suit'] = taozhuang[0]

                            print '这是武器【' + name + '】:' + json.dumps(wuqiary, encoding="UTF-8", ensure_ascii=False)
                            whattype = 'insert into t_armsdata set name='+name.replace('data_equip_name=','')+' , websiteid=' + '\"' + url + '\",' + parserSql(wuqiary)
                        #判断是防具
                        else:
                            for thekey in datas.split("#r"):
                                self.setArmordata(thekey,fangjuary)
                            print '这是防具：【' + name + '】:' + json.dumps(fangjuary, encoding="UTF-8", ensure_ascii=False)
                            whattype = 'insert into t_armordata set name='+name.replace('data_equip_name=','')+', websiteid=' + '\"' + url + '\",' + parserSql(fangjuary)
                    else:
                        for thekey in datas.split("#r"):
                            self.setArmordata(thekey, fangjuary)

                        print '这是防具：【' + name + '】:' + json.dumps(fangjuary, encoding="UTF-8", ensure_ascii=False)
                        whattype = 'insert into t_armordata set name='+name.replace('data_equip_name=','')+', websiteid='+'\"'+url+'\",'+parserSql(fangjuary)


                print whattype



            return ""
            # strinfo = re.compile('<[\s\S]*?>')
            # b = strinfo.sub('', matchObj.group())
            # return str(b.replace(reme, "").replace(" ", ""))
        except ValueError, Argument:
            print 'craw failed' ,Argument
            return ""

    def getParserEquip(self, role,content):
        try:
            matchObj = re.search(r''+role+'', str(content), re.M | re.I)
            if matchObj:
                return matchObj.group()
            return ""

        except:
            return ""

    def setDictData(self, onevalue,twovalue,thekey,dictionary):
        if twovalue in dictionary.keys():
            dictionary[twovalue] = dictionary[twovalue] + str(thekey).replace(
                onevalue + " ", '')
        else:
            dictionary[str(twovalue)] = str(thekey).replace(onevalue + " ", '')




    #防具解析
    def setArmordata(self,thekey,dictionary):
        if '五行' in thekey:
            thislevel = re.search(r'[0-9]+',thekey, re.M | re.I)
            dictionary['level'] = thislevel.group()

        elif '耐久度' in thekey:
            naijiu = re.findall(r'[0-9]+', thekey)
            count = 0
            datas=''
            for val in naijiu:
                if count == 0:
                    datas = val
                else:
                    datas = datas+','+val
                count += 1
            dictionary['durable'] = datas
        elif '防御' in thekey and '符石' not in thekey:
            thetest = re.findall(r'防御[^\u4e00-\u9fa5]+[0-9]+', thekey)
            getthevalue=''
            for va in thetest:
                getthevalue=va
            dictionary['defense']=getthevalue.replace("防御 ",'')

        elif '气血' in thekey and '符石' not in thekey:

            thetest = re.findall(r'气血[^\u4e00-\u9fa5]+[0-9]+', thekey)
            getthevalue = ''
            for va in thetest:
                getthevalue = va
            dictionary['blood']=getthevalue.replace("气血 ",'')
        elif '敏捷' in thekey and '符石' not in thekey:
            thetest = re.findall(r'敏捷[^\u4e00-\u9fa5]+[0-9]+', thekey)
            getthevalue = ''
            for va in thetest:
                getthevalue = va
            dictionary['speed']=getthevalue.replace("敏捷 ",'')
        elif '魔法' in thekey and '符石' not in thekey:

            thetest = re.findall(r'魔法[^\u4e00-\u9fa5]+[0-9]+', thekey)
            getthevalue = ''
            for va in thetest:
                getthevalue = va
            dictionary['magicpower']=getthevalue.replace("魔法 ",'')
        elif '灵力' in thekey and '符石' not in thekey:
            thetest = re.findall(r'灵力[^\u4e00-\u9fa5]+[0-9]+', thekey)
            getthevalue = ''
            for va in thetest:
                getthevalue = va
            dictionary['mana'] = getthevalue.replace("灵力 ",'')
        elif '锻炼等级' in thekey:

            duanliandengji = re.search(r'[0-9]+', thekey)

            duanlianbaoshi = re.search(r'宝石[\s\S]*', thekey)

            dictionary['exercise'] = duanliandengji.group()

            dictionary['gemstone'] = duanlianbaoshi.group().replace('宝石 ', '')

        elif '#G#G' in thekey:

            fujia = re.findall(r'[^\u4e00-\u9fa5]+[0-9]+', thekey)

            count = 0

            for val in fujia:

                if count == 0:
                    dictionary['fujia'] = val
                else:
                    dictionary['fujia'] = dictionary['fujia'] + val

                count += 1


        elif '特技' in thekey:

            teji = re.findall(r'[^\u4e00-\u9fa5^#]+', thekey)

            dictionary['stunt'] = teji[1]

        elif '特效' in thekey:

            texiao = re.findall(r'[^\u4e00-\u9fa5^#]+', thekey)

            dictionary['effects'] = texiao[1]

        elif '开运孔数' in thekey:

            kaikong = re.findall(r'[\u4e00-\u9fa5]+', thekey)

            dictionary['holenum'] = kaikong[1]

        elif '熔炼效果' in thekey:

            ronglian = re.findall(r'[+|-][0-9]+[^\u4e00-\u9fa5]* ', thekey)
            thrules=''
            for num in range(len(ronglian)):
                if num==0:
                    thrules=ronglian[num]
                else:
                    thrules=thrules+','+ronglian[num]

            dictionary['melting'] = thrules


        elif '套装效果' in thekey:

            taozhuang = re.findall(r'[^\u4e00-\u9fa5^#]+', thekey)

            dictionary['suit'] = taozhuang[0]

def process(url):
    print url

    obj_spider = HtmlDownloader()
    obj_spider.download(str(url))
def parserSql(df):
    dff = df.copy()
    for val in df:
        if len(dff[val]) == 0:
            del dff[val]
        if '#G' in df[val]:
            df[val] = dff[val].split('#G')[0]
            for ii in range(len(dff[val].split('#G')) - 1):

                if 'fujia' in dff.keys():
                    dff['fujia'] = dff['fujia'] + ',' + val + dff[val].split('#G')[ii + 1].replace('#cEE82EE[','').replace(']', '')
                else:
                    dff['fujia'] = val + dff[val].split('#G')[ii + 1].replace('#cEE82EE[', '').replace(']', '')

            if len(dff[val].split('#G')[0]) == 0:
                del dff[val]
            elif len(dff[val]) == 0:
                del dff[val]
    for parserInt in dff:
        try:
            dff[parserInt]=int(dff[parserInt])
        except :
            pass
    sts = json.dumps(dff, encoding="UTF-8", ensure_ascii=False)
    thekey = sts.encode("utf-8").replace('\":','=').replace(', \"',',').replace("{\"",'').replace('\"}','').replace('}','')
    return thekey


if __name__=="__main__":
    obj_spider = HtmlDownloader()
    for url in obj_spider.urls.get_all_url():
        p = multiprocessing.Process(target=process, args=(url,))
        p.start()



