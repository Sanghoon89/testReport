#!/usr/service/VENV/bin/python

import pymysql.cursors
import requests, locale

from datetime import datetime, date, timedelta

## 날짜
locale.setlocale(locale.LC_ALL,'')
YESTERDAY = date.today() - timedelta(1)
DATE = YESTERDAY.strftime('%Y-%m-%d')

conn = pymysql.connect(host='180.70.98.216', user='root', password='collect123$', db='tsmbackup', charset='utf8')
curs = conn.cursor()

SQL = f"select * from tsmEventLog where Date = '{DATE}' ORDER BY Date, Domain, Scheduled "
SQL_2 = f"select * from tsmRemoteKeep where check_date = '{DATE}' ORDER BY check_date, pool_name, volume_name "

curs.execute(SQL)
RESULT = curs.fetchall()

curs.execute(SQL_2)
RESULT_2 = curs.fetchall()

conn.close()

TableName = "EventLog"
Columns = "backup_dt,schedule_tm,schedule_nm,nodename,domain_nm,start_tm,end_tm,taken,status,returncode,action,note,modify_dt"

TableName_2 = "RemoteKeep"
Columns_2 = "check_dt, volume_nm, pool_nm, cycle, due_dt, safein_chk, safeout_chk"

for VALUES in list(RESULT):

    conn = pymysql.connect(host='localhost', user='root', password='xmflrj', db='myDjango', port=3456, charset='utf8')

    try:
        with conn.cursor() as cursor:
            SQL = f"INSERT INTO {TableName} ({Columns}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '', '',now())"
            print (SQL)
            cursor.execute(SQL, VALUES)

        conn.commit()

    except pymysql.err.IntegrityError as e :
        print ("Error: {}".format(e))

#    except MySQLdb.Error as e :
#        pass

    finally:
        conn.close()

for VALUES in list(RESULT_2):
    
    conn = pymysql.connect(host='localhost', user='root', password='xmflrj', db='myDjango', port=3456, charset='utf8')

    try:
        with conn.cursor() as cursor:
            SQL = f"INSERT INTO {TableName_2} ({Columns_2}) VALUES (%s, %s, %s, %s, %s, 'X', 'X')"
            print (SQL)
            cursor.execute(SQL, VALUES)

        conn.commit()

    except pymysql.err.IntegrityError as e :
        print ("Error: {}".format(e))

#    except MySQLdb.Error as e :
#        pass

    finally:
        conn.close()
