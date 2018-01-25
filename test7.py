#!/usr/bin/python
#coding:utf-8
import re


dictionary = {}

dictionary[str('dfe')] = str('ditj')


onevalue = '法术伤害'
twovalue = 'dspell'
if dictionary[twovalue]:
    dictionary[twovalue] = dictionary[twovalue] +  "dfdf"
else:
    dictionary[str(twovalue)] = "dfdf"



print str(dictionary).decode('unicode-escape')
for key in sorted(dictionary.keys()):            # yes
    print "该单词存在! " ,key, dictionary[key]
