import cx_Oracle

class reviewDB():

    def __init__(self,user):
        self.user=user


    def get_con(self):
        # db1=cx_Oracle.connect('system/123456@172.16.206.144:1521/SYS')
        self.db1=cx_Oracle.connect(self.user, "oracle", "192.168.3.46:1521/orcl.oracle.com")
        # sql = "select * from SCOTT.DEPT"


    def review(self,sql):
        cursor = self.db1.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

reviewDB1=reviewDB('system')
sql = "select * from SCOTT.DEPT"
reviewDB1.get_con()
result=reviewDB1.review(sql)
# if __name__=='main':

print(result)




# db1=cx_Oracle.connect("system", "oracle", "192.168.3.46:1521/orcl.oracle.com")
# sql = "select * from SCOTT.DEPT"
# cursor= db1.cursor()
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)



