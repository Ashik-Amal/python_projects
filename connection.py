import pymysql
myconnection =pymysql.connect(
    host='localhost',
    user='root',
    passwd='root',
    port=3306,
)
newscript = myconnection.cursor()
newscript.execute("show databases")
