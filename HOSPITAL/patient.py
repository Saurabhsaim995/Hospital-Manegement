import os
import time
from datetime import datetime as dd
import sys
import pwinput as pi

import pymysql as pm
import prettytable as pt
from helper import *
#=============================================
#GLOBAL VARIABLES
usr='root';pwd='root'; db='hospital_db'
gapvalue=30
maxid=None

#=============================================
def add_patient():
    print(' '*gapvalue,'A D D     N E W     P A T I E N T')
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor() 
        while(1):
            pid=getmaxNum('pid','patient')
            print(' '*gapvalue,'PATIENT ID:',pid); 
            print(' '*gapvalue,'INPUT FIRST NAME:',end=' ');pfname=input('')
            print(' '*gapvalue,'INPUT LAST NAME:',end=' ');plname=input('')
            print(' '*gapvalue,'INPUT GENDER [M|F]:',end=' ');gender=input('')
            print(' '*gapvalue,'INPUT CITY:',end=' ');city=input('')
            
            print(' '*gapvalue,'INPUT AGE:',end=' ');age=int(input(''));
            #print(' '*gapvalue,'INPUT ADMIT-DATE:',end=' ');sdoa=input(''); doa=dd.strftime(dd.now(),'%Y-%m-%d')
            print(' '*gapvalue,'INPUT mobile:',end=' ');mob=input('')
            view_All_doct()
            print(' '*gapvalue,'CHOOSE DOCTOR-ID TO refer:',end=' ');refer_to_dr=int(input(''))

            print(' '*gapvalue,'SYMPTOMS:',end=' ');symptom=input('')
            print(' '*gapvalue,'CONSULTATION FEE:',end=' ');consult_fee=float(input(''))
            
            qry=f"INSERT INTO patient(pid,pfname,plname,gender,city,age,doa,mob,refer_to_dr,symptom,consult_fee) \
VALUES({pid},'{pfname}','{plname}','{gender}','{city}',{age},DATE(SYSDATE()),'{mob}','{refer_to_dr}','{symptom}',{consult_fee})"
            cur.execute(qry) 
            con.commit()
            print(' '*gapvalue,'PATIENT REGISTERED SUCCESSFULLY  ')

            print(' '*gapvalue,'DO YOU WANT TO ADD ONE MORE EMPLOYEES ?\n Press [Y|y]: ',end='')
            choice=input('')
            if choice.lower()!='y':
                break
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#=========================================================

def update_patient(u_pid):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        #========================================
        #print(' '*gapvalue,'PATIENT ID:',pid); 
        print(' '*gapvalue,'INPUT FIRST NAME:',end=' ');pfname=input('')
        print(' '*gapvalue,'INPUT LAST NAME:',end=' ');plname=input('')
        print(' '*gapvalue,'INPUT GENDER [M|F]:',end=' ');gender=input('')
        print(' '*gapvalue,'INPUT CITY:',end=' ');city=input('')
        
        print(' '*gapvalue,'INPUT AGE:',end=' ');age=int(input(''));
        #print(' '*gapvalue,'INPUT ADMIT-DATE:',end=' ');sdoa=input(''); doa=dd.strftime(dd.now(),'%Y-%m-%d')
        print(' '*gapvalue,'INPUT mobile:',end=' ');mob=input('')
        view_All_doct()
        print(' '*gapvalue,'CHOOSE DOCTOR-ID TO refer:',end=' ');refer_to_dr=int(input(''))

        print(' '*gapvalue,'SYMPTOMS:',end=' ');symptom=input('')
        print(' '*gapvalue,'CONSULTATION FEE:',end=' ');consult_fee=float(input(''))

        qry=f"UPDATE patient SET pfname='{pfname}',plname='{plname}',gender='{gender}',city='{city}',age={age},doa=sysdate(),mob='{mob}',\
 refer_to_dr={refer_to_dr},symptom='{symptom}',consult_fee={consult_fee} WHERE pid={u_pid}"
        cur.execute(qry)
        con.commit()
        print(' '*gapvalue,'PATIENT DETAILS UPDATED')

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
#-----------------------------------------------------------
def delete_dept(u_dno):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        qry=f"DELETE FROM dept where dno={u_dno}"
        #print(qry);input()
        cur.execute(qry)
        con.commit()
        print(' '*gapvalue,'\nONE RECORD DELETED')

    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


#==================================================================================
def view_jobwise_emp():
    
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['JOBTITLE', "TOTAL EMPLOYEES"])
        
        qry=f"select jobtitle,count(*) from emp,job WHERE emp.jobid=job.jobid GROUP BY jobtitle"
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
    
#========================================
def view_deptwise_emp():
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['DEPARTMENT', "No. OF EMPLOYEES"])
        
        qry=f"select dname,count(*) from emp,dept WHERE emp.dno=dept.dno GROUP BY dname"
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

    
#------------------------------------------
def view_all_emp():
    
    print(' '*gapvalue,'    [EMPLOYEE LIST] ')
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['ENo',' FIRST NAME','LAST NAME','DEPARTMENT', 'CITY','HIRE-DATE','JOBTIITLE','SALARY'])
        qry=f"select eno,fname,lname,dname,loc,hire_date,jobtitle,basic+grade+(basic*0.01*da)+(basic*0.01*hra)-(basic*0.01*tax)+(basic*ifnull(comm,0)*0.01)  SALARY \
from emp,job,dept WHERE emp.jobid=job.jobid AND emp.dno=dept.dno"
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

#========================================================
def viewdeptbydno(u_dno):
    
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['DID',' DEPARTMENT NAME','CITY'])
        qry=f"select * from DEPT WHERE dno={u_dno}"
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
    
#----------------------------------------
def search_by_mob(u_mob):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['MEMBER ID',' NAME','MOBILE','CITY','ID-PROOF','ID-No.','FEE','REGISTRATION DATE','FINE'])
        qry=f"select * from member WHERE mob LIKE '%{u_mob}%'"
        cur.execute(qry)
        rows=cur.fetchall()
        if rows==():
            print(' '*gapvalue,'RECORD NOT FOUND')
        else:
            for r in rows:
                t.add_row([r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]])
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
#--------------END OF EMP.PY-----------
