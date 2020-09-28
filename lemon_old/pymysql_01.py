import pymysql

con = pymysql.connect(
                host='47.100.25.73',
                port=3309,
                user='masteropr',
                passwd='6Gm(i_eRa*g>',
                charset='utf8'
)


sql ='create database yldb character set =UTF8MB4'
# sql1= "GRANT SELECT,INSERT,DELETE,UPDATE ON jiradb.* TO 'jiraopr'@'%'"
# sql1 = "show databases"




cursor = con.cursor()
cursor.execute(sql)
con.commit()
res =cursor.fetchall()
print(res)
cursor.close()
con.close()













