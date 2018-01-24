#coding:utf-8
'''
Created on 2017 2017-7-28 上午11:25:00

@author: Alan
'''
from sqls import MSSQL
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>")
        fout.write("<body>")
        fout.write("<table  border='8'>")

        for data in self.datas:
            # if data['content']!='1'and data['content'] is not None:
            #     ms = MSSQL(host="192.168.1.100", user="sa", pwd="123456", db="DataFactory")
            #     contentsdata=str(data['content']).replace('\'','\"')
            #
            #     newdata=contentsdata.replace('<p> </p>','')
            #     thesql = "insert into t_workbench_taskDetail  (content,taskId,status) VALUES ('"+newdata+"',6,0) ".encode("utf8")
            #     ms.ExecNonQuery(thesql)
            # ms.insertDate(data['content'])

            ##      resList = ms.ExecQuery("SELECT id FROM t_base_admin")
            ##      ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['content'].encode('utf-8'))
            fout.write("</tr>")
         
         
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

    
    
    

