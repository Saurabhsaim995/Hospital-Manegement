import os
import time
import pymysql as pm
#=============================================
def install_pymysql():
    os.system('cmd /c "cd\\users\\dell"');
    os.system('cmd /c "python -m pip install -U pymysql"')

def install_prettytable():
    os.system('cmd /c "cd\\users\\dell"');
    os.system('cmd /c "python -m pip install -U prettytable"')


#=============================================
def initmod():
    print('SETUP INITIATED.....')
    time.sleep(1)
    print('Checking...PRETTYTABLE')
    time.sleep(1)

    try:
        import prettytable as pt
    except ModuleNotFoundError:
        print('NO MODULE PRETTYTABLE')
        print('Installing Module...')
        install_prettytable()
        print(f'Module PRETTYTABLE Installed Successfully')
    print('DONE')
    print('Checking...PYMYSQL')
    time.sleep(1)

    try:
        import pymysql as pm
    except ModuleNotFoundError:
        print('NO MODULE PYMYSQL')
        print('Installing Module...')
        install_pymysql()
        print(f'Module PYMYSQL Installed Successfully')
    print('DONE')
#=============================================
#=============================================
def setup_database():
    try:
        qry='CREATE DATABASE IF NOT EXISTS hopital_db'
        con=pm.connect(user='root',password='root',host='localhost')
        if con is not None:
            print('Connection Successful')
            cur=con.cursor()
            cur.execute(qry)
            print('DATABASE CREATED SUCCESSFULLY')
        else:
            print('Error')
    except pm.DatabaseError as e:
        con.rollback()
        print(e)
    finally:
            if cur is not None:
                cur.close()
            if con is not None:
                con.close()
#=====================================================================
def setup_personal():
    try:
        qry="CREATE TABLE IF NOT EXISTS PERSONAL( cno INT PRIMARY KEY, cname VARCHAR(30),\
CITY VARCHAR(20),GENDER VARCHAR(6),PH VARCHAR(45),EMAIL VARCHAR(45),MINORITY VARCHAR(6),\
ADDR VARCHAR(45),MOBILE VARCHAR(12),DOB DATE,MARITAL VARCHAR(45),PASSWD VARCHAR(45));"
        con=pm.connect(user='root',password='root',host='localhost',db='upsc')
        cur=con.cursor()
        cur.execute(qry)
        print('Table Created Successfully')
    except pm.DatabaseError as e:
        con.rollback()
        print('Something Wrong:=>',e)
    finally:
        if cur is not None:
                cur.close()
        if con is not None:
                con.close()

#==============================================================================
initmod()
setup_database()
