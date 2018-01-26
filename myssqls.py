#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class DoSql(object):
    def insertData(self,sql):

        # 打开数据库连接
        db =MySQLdb.connect(111)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()


        db.close()

    def selectDate(self,sql):
        # 打开数据库连接
        db = MySQLdb.connect(111)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                      (fname, lname, age, sex, income )
        except:
            print "Error: unable to fecth data"
        db.close()

    def updateDate(self,sql):
        # 打开数据库连接
        db = MySQLdb.connect(111)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

            # 关闭数据库连接
            db.close()

    def selectUrl(self,sql):
        # 打开数据库连接
        db = MySQLdb.connect(111)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            allUrls=set()
            for row in results:
                allUrls.add(row[0])
                # print "url=%s" % row[0]
                # 打印结果
            return  allUrls
        except:
            print "Error: unable to fecth data"
        db.close()

    def selectOldUrl(self):
        sql = "select websiteid from t_roleData    \
                        where issell ='否' "
        thetest = DoSql();
        return thetest.selectUrl(sql)
    def selectNewUrl(self):
        sql = "select websiteid from t_roleData    \
                        where crawler =0 "
        thetest = DoSql();
        return thetest.selectUrl(sql)



if __name__ == "__main__":
    sql = "INSERT INTO t_petdata(websiteid, \
                   servicearea, rolewebsiteid, sellername, sellerid) \
                   VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
          ('www.baidu.com', '如意岛2', '345345', '霸气哥', '007')
    sql1 = "INSERT INTO t_roleData(websiteid, \
                   number, sellerid, puton, servicearea) \
                   VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
          ('www.baidu.com', '如意岛2', '345345', '霸气哥', '007')
    thetest=DoSql();
    thetest.selectOldUrl()



