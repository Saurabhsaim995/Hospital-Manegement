import pymysql as pm
import prettytable as pt
from datetime import datetime as dd
import pwinput as pi
#---------------------
maxid=''
gapvalue=30
usr='root';pwd='root'; db='hospital_db';
#--------------------
def getmaxNum(colnm,tblnm):
    global maxid
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"select max({colnm}) from {tblnm}"
        cur.execute(qry) 
        row=cur.fetchone() #(None,)
        if row[0]==None:
            maxid=1
        else:
            maxid=row[0]+1
    except pm.DatabaseError as e:
        con.rollback()
        print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return maxid

#------------------------
def isValid_id(tblnm,colnm,colval):
    try:
        found=''
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"select * from {tblnm} WHERE {colnm} ={colval}"
        #print(qry)
        cur.execute(qry)
        r=cur.fetchone()
        print(r)
        if r==None:
            print(' '*gapvalue,'RECORD NOT FOUND')
            found=False
        else:
            #t.add_row(r)
            #print()
            found=True
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return found

#===================
def isValid_pid_did(pid,did):
    try:
        found=''
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"select * from patient WHERE refer_to_dr ={did} AND pid={pid}"
        #print(qry)
        cur.execute(qry)
        r=cur.fetchone()
        #print(r)
        if r==None:
            print(' '*gapvalue,'RECORD NOT FOUND')
            found=False
        else:
            #t.add_row(r)
            #print()
            found=True
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return found

#==================
def isauth_user(upass):
    if upass=='123':
        return True
    else:
        return False
#==================
def getTableHeader(tblnm):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"select column_name FROM information_schema.columns WHERE table_schema='{db}' AND table_name='{tblnm}';"
        cur.execute(qry)
        rows=cur.fetchall()
        headLst=[]
        for i in rows:
            headLst.append(i[0])
        

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return headLst
#======================================
def viewAllRecords(tblnm):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        head=getTableHeader(tblnm)
        t=pt.PrettyTable()
        t.field_names=(head)
        qry=f"select * from {tblnm}"
        cur.execute(qry)
        rows=cur.fetchall()
        if rows==():
            print(' '*gapvalue,'RECORD NOT FOUND')
        else:
            for r in rows:
                t.add_row(r)
            print(t)
            print(' '*gapvalue,'Total {} records fetched. '.format(len(rows)))
                
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
#=====================================
def viewAllRecords_by_id(tblnm,colnm,colval):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        head=getTableHeader(tblnm)
        t=pt.PrettyTable()
        t.field_names=(head)
        qry=f"select * from {tblnm} WHERE {colnm}={colval}"
        cur.execute(qry)
        rows=cur.fetchall()
        if rows==():
            print(' '*gapvalue,'RECORD NOT FOUND')
        else:
            for r in rows:
                t.add_row(r)
            print(t)
            print(' '*gapvalue,'Total {} records fetched. '.format(len(rows)))
                
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#=====================================
def delete_record_by_id(tblnm,colnm,colval):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"DELETE FROM {tblnm} where {colnm}={colval}"
        #print(qry);input()
        cur.execute(qry)
        con.commit()
        print('\n',' '*gapvalue,'ONE RECORD DELETED')

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
#--------------END OF HELPER.PY--------
def view_All_doct():
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['DID',' DOCTOR NAME','SPECIALIST'])
        qry=f"select did,concat(dfname,' ',dlname),speciality from doctor"
        cur.execute(qry)
        rows=cur.fetchall()
        if rows==():
            print(' '*gapvalue,'RECORD NOT FOUND')
        else:
            for r in rows:
                t.add_row([r[0],r[1],r[2]])
            print(t)
            print(' '*gapvalue,'Total {} records fetched. '.format(len(rows)))
                
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
#========================================
def get_doctor_id_pass(u_did):
    did,passwd=None,None
    try:
        
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"select did,password from doctor WHERE did={u_did}"
        cur.execute(qry)
        r=cur.fetchone()
        #print(r)
        if r==None:
            did,passwd=None,None
            print(' '*gapvalue,'INVALID DOCTOR ID / PASSWORD')
        else:
            did,passwd=r[0],r[1]
            #print(did,passwd)
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return r[0],r[1]
#----------------------------------------
def doctor_Login(did):
    status=False
    print(' '*gapvalue,'INPUT PASSWORD:',end=' ');        passwd=pi.pwinput(prompt="")

    u_did,udpass=get_doctor_id_pass(did)
    if u_did==None and udpass==None:
        print(' '*gapvalue,'LOGIN FAILED')
        status=False
    elif did==u_did and passwd==udpass:
        
        print(' '*gapvalue,'LOGIN SUCCESSFUL')
        status=True
    else:
        print(' '*gapvalue,'LOGIN FAILED')
        status=False
    return status
#----------------------------------------
def getpatentby_drid(did):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['PID','PATIENT NAME','SPECIALIST'])
        qry=f"select did,concat(dfname,' ',dlname),speciality from doctor"
        cur.execute(qry)
        rows=cur.fetchall()
        if rows==():
            print(' '*gapvalue,'RECORD NOT FOUND')
        else:
            for r in rows:
                t.add_row([r[0],r[1],r[2]])
            print(t)
            print(' '*gapvalue,'Total {} records fetched. '.format(len(rows)))
                
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
    
