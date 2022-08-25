import pymysql as sql

myobj = sql.connect(host='localhost',user='root',password='',database='testProject')

try :
    sq=myobj.cursor()
    print("connected")

except: 
    print("error")