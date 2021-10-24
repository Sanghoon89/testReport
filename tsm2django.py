#!/usr/service/VENV/bin/python

import pymysql.cursors
import locale

from datetime import datetime, date, timedelta

# 날짜
locale.setlocale(locale.LC_ALL, '')
YESTERDAY = date.today() - timedelta(1)
DATE = YESTERDAY.strftime('%Y-%m-%d')

SQL_1 = f"select * from tsmEventLog where Date = '{DATE}' ORDER BY Date, Domain, Scheduled "
TableName_1 = "EventLog"
Columns_1 = "backup_dt,schedule_tm,schedule_nm,nodename,domain_nm,start_tm,end_tm,taken,status,returncode,action,note,modify_dt"
INSQL_1 = f"INSERT INTO {TableName_1} ({Columns_1}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '', '',now())"

SQL_2 = f"select * from tsmRemoteKeep where check_date = '{DATE}' ORDER BY check_date, pool_name, volume_name "
TableName_2 = "RemoteKeep"
Columns_2 = "check_dt, volume_nm, pool_nm, cycle, due_dt, safein_chk, safeout_chk"
INSQL_2 = f"INSERT INTO {TableName_2} ({Columns_2}) VALUES (%s, %s, %s, %s, %s, 'x', 'x')"


#conn = pymysql.connect(host='192.168.15.11', user='root', password='xmflrj', db='tsmBackup', charset='utf8')
conn = pymysql.connect(host='180.70.98.216', user='root',
                       password='collect123$', db='tsmbackup', charset='utf8')
curs = conn.cursor()
for i in range(1, 3):
    curs.execute(globals()[f'SQL_{i}'])
    globals()[f'RESULT_{i}'] = curs.fetchall()
conn.close()


for i in range(1, 3):
    for VALUES in list(globals()[f'RESULT_{i}']):
        conn = pymysql.connect(host='localhost', user='root',
                               password='xmflrj', db='myDjango', port=3456, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(globals()[f'INSQL_{i}'], VALUES)

            conn.commit()

        except pymysql.err.IntegrityError as e:
            print("Error: {}".format(e))

    #    except MySQLdb.Error as e :
    #        pass

        finally:
            conn.close()
