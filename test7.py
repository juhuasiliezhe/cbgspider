#!/usr/bin/python
#coding:utf-8
import re
import json
class HtmlDownloader(object):
    def setDictData2(self):
        thislevel = re.search(r'[0-9]+', '[<table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr><td class="noData">无</td></tr> </tbody></table>, <table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr> <th>祥瑞总数</th> <td>1</td> </tr> <tr> <th>流云玉佩</th> <td>技能：                          无            			          </td> </tr> </tbody></table>]')
        thetest=re.findall(r'<th[\s\S]*?</th>','[<table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr><td class="noData">无</td></tr> </tbody></table>, <table cellpadding="0" cellspacing="0" class="tb02" id="RoleXiangRui"> <tbody><tr> <th>祥瑞总数</th> <td>1</td> </tr> <tr> <th>流云玉佩</th> <td>技能：                          无            			          </td> </tr> </tbody></table>]')
        for val in thetest:
            print val





    def setDictData(self, onevalue,twovalue,thekey,dictionary):
        if twovalue in dictionary.keys():
            dictionary[twovalue] = dictionary[twovalue] + str(thekey).replace(
                onevalue + " ", '')
        else:
            dictionary[str(twovalue)] = str(thekey).replace(onevalue + " ", '')

if __name__ == "__main__":
    obj_spider = HtmlDownloader()
    obj_spider.setDictData2()


