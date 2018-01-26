#!/usr/bin/python
#coding:utf-8
import re
import json
class HtmlDownloader(object):
    def setDictData2(self):
        dictionary = {}
        dictionary2 = {}

        dictionary['dfe2'] = 'ditj'

        onevalue='e2'
        twovalue='dfe24'
        thekey='88888e2'
        self.setDictData(onevalue,twovalue,thekey,dictionary2)
        self.setDictData(onevalue,twovalue,thekey,dictionary)
        print json.dumps(dictionary, encoding="UTF-8", ensure_ascii=False)
        print json.dumps(dictionary2, encoding="UTF-8", ensure_ascii=False)



    def setDictData(self, onevalue,twovalue,thekey,dictionary):
        if twovalue in dictionary.keys():
            dictionary[twovalue] = dictionary[twovalue] + str(thekey).replace(
                onevalue + " ", '')
        else:
            dictionary[str(twovalue)] = str(thekey).replace(onevalue + " ", '')

if __name__ == "__main__":
    obj_spider = HtmlDownloader()
    obj_spider.setDictData2()


