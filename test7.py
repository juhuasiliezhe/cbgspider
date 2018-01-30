#!/usr/bin/python
#coding:utf-8
import re
import json
class HtmlDownloader(object):
    def setDictData2(self):
        thislevel = re.search(r'类型[\s\S]*?</td>', '<table cellpadding="0" cellspacing="0" class="tb02" width="100%"> <tbody><tr> <th>类型：</th> <td>云魅仙鹿</td> <th>主属性：</th> <td>未选择</td> </tr> <tr> <th>等级：</th> <td>170</td> <th> </th> <td> </td> </tr> <tr> <th>成长：</th> <td>2.2647</td> <th> </th> <td> </td> </tr></tbody></table>, <table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr><td class="noData">无</td></tr> </tbody></table>, <table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr><td class="noData">无</td></tr> </tbody></table>] ')
        thetest=re.findall(r'[+|-][0-9]+[^\u4e00-\u9fa5]* ','#Y熔炼效果：#r#Y#r+8防御 -2敏捷 ')
        # print thislevel.group()
        # for val in thetest:
        #     print val
        getskill=['df','fdg','fg']
        theallkill = ''
        for vals in range(len(getskill)):
            theallkill += getskill[vals]+','
        print theallkill




    def setDictData(self, onevalue,twovalue,thekey,dictionary):
        if twovalue in dictionary.keys():
            dictionary[twovalue] = dictionary[twovalue] + str(thekey).replace(
                onevalue + " ", '')
        else:
            dictionary[str(twovalue)] = str(thekey).replace(onevalue + " ", '')

if __name__ == "__main__":
    obj_spider = HtmlDownloader()
    obj_spider.setDictData2()


