#!/usr/bin/python3
import MySQLdb
#python.exe -m pip install --upgrade pip
#pip install mysqlclient
#--------------------------------------------------------------------------------

def insertpersonSimpleInfo():
    db = MySQLdb.connect("cow8.cn", "root", "wo1274haoba", "shan", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone() 
    print ("Database version : %s " % data)

    for num in range(0,10):
        name="ffff"
        snum = str(num)
        sqlstr="insert into personSimpleInfo(acc,experience,beGoodAt,tag) value(\"%s\",\"%s\",\"%s\",\"%s\");" \
         % (snum,"1.毕业北航。2.百度、360工作。3.连续创业者。","c++/vue/java/音视频","java c++ vue 音视频 直播 点播")
        print(sqlstr+"\r\n")
        try:
            cursor.execute(sqlstr)   
            db.commit()     
        except:        
            #db.rollback()
            print('insert error!')
        

    # 关闭数据库连接
    db.close()
#
insertpersonSimpleInfo()
#--------------------------------------------------------------------------------
def insertactiveTimeTable():
    db = MySQLdb.connect("cow8.cn", "root", "wo1274haoba", "shan", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone() 
    print ("Database version : %s " % data)

    for num in range(0,10):
        name="ffff"
        snum = str(num)
        sqlstr="insert into activeTimeTable(acc,activeTime) value(\"%s\",\"%s\");" % (snum,"2022-09-01 12:01:01")
        print(sqlstr+"\r\n")
        try:
            cursor.execute(sqlstr)   
            db.commit()     
        except:        
            #db.rollback()
            print('insert error!')
        

    # 关闭数据库连接
    db.close()
#
#insertactiveTimeTable()

#--------------------------------------------------------------------------------
def insertAcc():
    db = MySQLdb.connect("cow8.cn", "root", "wo1274haoba", "shan", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone() 
    print ("Database version : %s " % data)

    for num in range(0,10):
        name="ffff"
        snum = str(num)
        sqlstr="insert into acc(acc,pwd,name,isvip) value(\"%s\",\"%s\",\"%s\",\"%s\");"  \
        % (snum,snum,name,"false")
        print(sqlstr+"\r\n")
        try:
            cursor.execute(sqlstr)   
            db.commit()     
        except:        
            #db.rollback()
            print('insert error!')
        

    # 关闭数据库连接
    db.close()

#execute
#insertAcc()
