# #!/usr/bin/python
# # -*- coding:utf-8 -*-
import multiprocessing
from decimal import *
import torndb

def process(num):
    print 'Process:', num
    theprice = '15454.65'
    sql = "INSERT INTO t_roleData(websiteid,servicearea, issell, crawler,price) VALUES ('%s',  '%s', '%s', '%d', '%.2f' )" %( 'href', '黑龙江区 雪域天龙', '否', 0, float(theprice))
    print sql

    dff='15454.65'
    print float(dff)

if __name__ == '__main__':
   process(1)




def getTerm(db,tag):
    query = "SELECT term_id FROM wp_terms where name=%s "
    rows = db.query(query,tag)
    termid = []
    for row in rows:
      termid.extend(row.values())
    return termid
def addTerm(db,tag):
    query = "INSERT into wp_terms (name,slug,term_group) values (%s,%s,0)"
    term_id = db.execute_lastrowid(query,tag,tag)
    sql = "INSERT into wp_term_taxonomy (term_id,taxonomy,description) values (%s,'post_tag',%s) "
    db.execute(sql,term_id,tag)

    return term_id
def addCTag(db,data):
    query = "INSERT INTO wp_term_relationships (object_id,term_taxonomy_id) VALUES (%s, %s) "
    db.executemany(query,data)
dbconn = torndb.Connection('localhost:3306','361way',user='root',password='123456')


