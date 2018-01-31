# #!/usr/bin/python
# # -*- coding:utf-8 -*-
import multiprocessing
from decimal import *
import torndb
import json

def process(num):

    dff='{"skill": ["/images/pet_child_skill/0310.gif", "/images/pet_child_skill/0424.gif", "/images/pet_child_skill/0510.gif", "/images/pet_child_skill/0575.gif", "/images/pet_child_skill/0576.gif", "/images/pet_child_skill/0661.gif", "/images/pet_child_skill/0428.gif"], "name": "吸血鬼", "level": 180}'

    # thekey=dff.replace(': [','=').replace('\", \"/',',').replace(': ','=').replace(']','').replace('{','').replace('}','')
    thekey=dff.replace('{\"','').replace('[','').replace('\", \"/',',').replace('], \"',',').replace('\":','=')
    print  thekey



if __name__ == '__main__':
   process(1)




