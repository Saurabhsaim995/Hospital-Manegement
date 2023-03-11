import os
import time
from datetime import datetime as dd
import sys
import pwinput as pi
import pymysql as pm
import prettytable as pt
from helper import *
#=================================================
#GLOBAL VARIABLES
usr='root';pwd='root'; db='hospital_db'
gapvalue=30
maxid=None

#=================================================
def add_doct():
    print(' '*gapvalue,'A D D     N E W     D O C T O R ')
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor() 
        while(1):
            did=getmaxNum('did','doctor')
            print(' '*gapvalue,'DOCTOR-ID.:',did); 
            print(' '*gapvalue,'INPUT FIRST NAME:',end=' ');dfname=input('')
            print(' '*gapvalue,'INPUT LAST NAME:',end=' ');dlname=input('')
            print(' '*gapvalue,'INPUT GENDER [M|F]:',end=' ');gender=input('')
            while 1:
                print(' '*gapvalue,'CREATE PASSWORD:',end=' ');pass1=pi.pwinput(prompt="")
                print(' '*gapvalue,'RE-ENTER PASSWORD:',end=' ');pass2=pi.pwinput(prompt="")
                if pass1==pass2:
                    print(' '*gapvalue,'PASSWORD SET SUCCESSFULLY')
                    password=pass1
                    break
                        
                else:
                    print(' '*gapvalue,'PASSWORD MISMATCH! CREATE IT AGAIN !')
            
            print(' '*gapvalue,'INPUT SPECIALITY:',end=' ');speciality=input('')
            print(' '*gapvalue,'INPUT SHIFT [DAY | NIGHT]:',end=' ');shift=input('')
            print(' '*gapvalue,'INPUT MOBILE No:',end=' ');mob=input('')

            
            qry=f"INSERT INTO doctor VALUES({did},'{dfname}','{dlname}','{gender}','{password}','{speciality}','{shift}','{mob}')"
            cur.execute(qry) 
            con.commit()
            print(' '*gapvalue,'ONE DOCTOR REGISTERED')

            print(' '*gapvalue,'DO YOU WANT TO ADD ONE MORE doctor ?\n Press [Y|y]: ',end='')
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

def update_doct(u_did):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        print(' '*gapvalue,'INPUT FIRST NAME:',end=' ');dfname=input('')
        print(' '*gapvalue,'INPUT LAST NAME:',end=' ');dlname=input('')
        print(' '*gapvalue,'INPUT GENDER [M|F]:',end=' ');gender=input('')
        while 1:
            print(' '*gapvalue,'CREATE PASSWORD:',end=' ');pass1=pi.pwinput(prompt="")
            print(' '*gapvalue,'RE-ENTER PASSWORD:',end=' ');pass2=pi.pwinput(prompt="")
            if pass1==pass2:
                print(' '*gapvalue,'PASSWORD SET SUCCESSFULLY')
                password=pass1
                break
                    
            else:
                print(' '*gapvalue,'PASSWORD MISMATCH! CREATE IT AGAIN !')
        
        print(' '*gapvalue,'INPUT SPECIALITY:',end=' ');speciality=input('')
        print(' '*gapvalue,'INPUT SHIFT [DAY | NIGHT]:',end=' ');shift=input('')
        print(' '*gapvalue,'INPUT MOBILE No:',end=' ');mob=input('')


        qry=f"UPDATE doctor SET dfname='{dfname}',dlname='{dlname}',gender='{gender}',password='{pass1}',speciality='{speciality}',shift='{shift}',mob='{mob}' WHERE did={u_did}"
        cur.execute(qry)
        con.commit()
        print(' '*gapvalue,'DOCTORE DETAILS UPDATED')
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

#=================================
def view_patient_history():
    print(' '*gapvalue,'    H M S   [PATIENT HISTORY RECORDS] ')
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        t=pt.PrettyTable(['PATIENT NAME','DOCTOR','Admit date','REASON','SYMPTOMS','TREATEMENT','MEDICINE','DOSE','DAYS'])
        #                       0           1         2           3        4          5            6         7       8
        qry='''SELECT CONCAT(PFNAME,' ',PLNAME),CONCAT(DFNAME,' ',DLNAME),DOA,DISEASE_CAUSED_BY,SYMPTOMS,
                      TREATEMENT_DETAIL,PRESCRIBE_MEDICINE,DOSE,NO_OF_DAYS
               FROM TREATEMENT T,PATIENT P,DOCTOR D
               WHERE T.PID=P.PID AND D.DID=T.DID ;'''
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
def save_treatement(did):
    try:
        con=pm.connect(user=usr,password=pwd,host='localhost',database=db)
        cur=con.cursor()
        tno=getmaxNum('tno','treatement')
        print(' '*gapvalue,'INPUT PATIENT TREATEMENT DETAILS')
        print('*'*80)
        print(' '*gapvalue,'TREATEMENT-ID:',tno)
        while 1:
            print(' '*gapvalue,'INPUT PATIENT-ID:',end='');pid=int(input(''))
            if isValid_pid_did(pid,did)==True:
                break
            else:
                print('INVALID PATIENT ID! RE-ENTER CORRECT PATIENT-ID')
                
        print(' '*gapvalue,'INPUT DISEASE CAUSED BY:',end='');disease_caused_by=input('')
        print(' '*gapvalue,'INPUT SYMPTOMS OF DISEASE:',end='');symptoms=input('')
        print(' '*gapvalue,'INPUT TREATEMENT DETAILS:',end='');treatement_detail=input('')
        print(' '*gapvalue,'INPUT PRESCRIBED MEDICINES:',end='');prescribe_medicine=input('')
        print(' '*gapvalue,'INPUT DOSAGE:',end='');dose=input('')
        print(' '*gapvalue,'INPUT prescription number of days :',end='');no_of_days=int(input(''))

        qry= f""" INSERT INTO treatement  
                 values
                 ({tno},{pid},{did},'{disease_caused_by}','{symptoms}','{treatement_detail}','{prescribe_medicine}','{dose}',{no_of_days})
                 """
        cur.execute(qry)
        con.commit()
        print('*'*80)
        print(' '*gapvalue,'TREATEMENT DATA SAVED')
        print('*'*80)
        
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#-------------------------
