#coding=utf-8
import ibm_db,datetime,pymssql

def get_db2_con(conn_info):
    try:
        conn = ibm_db.connect(conn_info, "", "")
        return conn
    except Exception as e:
        print(e)

def get_ms_con(database):
    try:
        conn = pymssql.connect(
            host='10.46.21.173',
            user='sa',
            password='dfzq1234',
            database=database
        )
        return conn
    except Exception as e:
        print(e)

def exec_db2_131():
    date = datetime.datetime.now().strftime('%Y%m%d')
    conn_info = "DATABASE=KSDBS;HOSTNAME=10.45.6.131;PORT=50000;PROTOCOL=TCPIP;UID=rzrqbcc;PWD=rzrqbcc;"
    conn = get_db2_con(conn_info)
    print(conn)
    tablelist = ['ENTRUST', 'REAL_DONE', 'XY_ENTRUST', 'XY_REAL_DONE', 'TRANS_CFG', 'TRANS_PARTITION','BANK_TRF_INTERFACE']
    for table in tablelist:
        sql = "truncate table KS.%s immediate;" % table
        ibm_db.exec_immediate(conn, sql)

    # tablelist2 = ['ETF_BASE_INFO', 'ETF_BASKET_INFO']
    # for i in tablelist2:
    #     sql2 = "update KS.%s set TX_DATE = '%s';" % (i, date)
    #     print(sql2)
    #     ibm_db.exec_immediate(conn, sql2)
    #     print('exec end')
    print('131 完成')

def exec_db2_175():
    date = datetime.datetime.now().strftime('%Y%m%d')
    conn_info = "DATABASE=KSDBS;HOSTNAME=10.46.0.175;PORT=51000;PROTOCOL=TCPIP;UID=jzjybcc;PWD=y2iaciej;"
    print('start')
    conn = get_db2_con(conn_info)
    print(conn)
    tablelist = ['ENTRUST','REAL_DONE','XY_ENTRUST','XY_REAL_DONE','TRANS_CFG','TRANS_PARTITION']
    for table in tablelist:
        sql = "truncate table KS.%s immediate;" % table
        ibm_db.exec_immediate(conn, sql)

    tablelist2 = ['ETF_BASE_INFO','ETF_BASKET_INFO']
    for i in tablelist2:
        sql2 = "update KS.%s set TX_DATE = '%s';"%(i,date)
        print(sql2)
        ibm_db.exec_immediate(conn, sql2)
        print('exec end')
    print('175 完成')

def exec_ms_173(env):
    table_dict = {'RZRQ131':['ORDWTH','ORDWTH2','CJHB'],'JZJY175':['Ashare_ORDWTH','ashare_ORDWTH2','ashare_cjhb']}
    conn = get_ms_con(env)
    print(conn)
    cursor = conn.cursor()
    for i in table_dict[env]:
        sql='TRUNCATE TABLE %s;'%i
        print(sql)
        cursor.execute(sql)
        # rs = cursor.fetchall()
        # print(rs)
    print('【173执行完成】')



if __name__ == '__main__':
    exec_db2_175()
    exec_db2_131()
    exec_ms_173('RZRQ131')
    exec_ms_173('JZJY175')





