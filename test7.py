#!/usr/bin/python
import re
a = 'hello word dfword<idf>,<li>'
strinfo = re.compile('<[\s\S]*?>')
b = strinfo.sub('python',a)
print b