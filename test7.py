#!/usr/bin/python
#coding:utf-8
import re
import json


dictionary = {}

dictionary[str('dfe')] = str('ditj')



thevalue='<img id="role_using_equip_190" width="50" height="50" data_equip_name="莲音玦" data_equip_type="27303" data_equip_desc="等级 100#r速度 +17#r耐久度 90#r精炼等级 1#r#G防御 +21 #cEE82EE[+8]#r#G格挡值 +28 #cEE82EE[+8]#r#W制造者：乱世何来佳人强化打造#" data_equip_type_desc="仙池清莲所化的玉玦，隐隐可闻其中仙音缭绕，长佩于身，有助修行。#r【装备条件】等级100#r【灵饰类型】佩饰" src="http://res.xyq.cbg.163.com/images/equip/small/27303.gif" lock_types="1">'
for thekey in thevalue.split("#r"):
    print thekey




