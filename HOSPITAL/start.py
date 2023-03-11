import os
import time
from datetime import datetime as dd
import sys
import pwinput as pi 
import pymysql as pm
import prettytable as pt
from doctor import *
from helper import *
from patient import *

#=============================================================================================
#GLOBAL VARIABLES
usr='root';pwd='root'; db='hospital_db'
gapvalue=30
maxid=None
maintitle='  HOSPITAL MGMT. SYSTEM    '
mainmenu=f'''
         ==================================================================================================================
         |      H O S P I T A L      M G M T.     S Y S T E M         -         M A I N     M E N U                       |
         ==================================================================================================================
         |*|  DOCTOR     |1|  NEW DOCTOR     |2|  VIEW ALL DOCTORs       |3|  MODIFY DETAILS.   |4| DELETE DOCTOR .       |
         ------------------------------------------------------------------------------------------------------------------
         |*|  PATIENT    |5|  NEW PATIENT    |6|  VIEW ALL PATIENTs      |7|  MODIFY PATIENT    |8| DELETE PATIENT        | 
         ------------------------------------------------------------------------------------------------------------------
         |*|  TREATEMENT |9|  NEW TREATEMENT |10| VIEW BY PATIENT        |11| VIEW TREATEMENT HISTORY |12|   E X I T      |
         ==================================================================================================================
       '''
os.system('cls')

print(' '*gapvalue,'L O G I N   F O R M')
print(' '*gapvalue,'Input ',end='');upass=pi.pwinput()
if upass=='123':
    print(' '*gapvalue,'LOGIN SUCCESSFUL \n',' '*gapvalue,'PRESS ENTER KEY TO RUN APPLICATION >>>');
    input()
    while 1:
        print(mainmenu)
        print(' '*gapvalue,'INPUT YOUR CHOICE [0-12]: ',end='')
        ch=input('')
        print('='*120)
        #doctor menu
                
        if(ch=='1'):
            #New doct
            print(' '*gapvalue,'ENTER PASSWORD: ',end=''); admPass=pi.pwinput(prompt='')
            if not isauth_user(admPass):
                print(' '*gapvalue,'INVALID PASSWORD! PRESS ENTER KEY TO CONTINUE')
            else:
                add_doct()
        elif (ch=='2'):
            #View All Doc
            viewAllRecords('doctor')
        elif(ch=='3'):
            #modify doc
            print(' '*gapvalue,'Input ',end='');admPass=pi.pwinput()
            if not isauth_user(admPass):
                print(' '*gapvalue,'INVALID PASSWORD! PRESS ENTER KEY TO CONTINUE')
            else:
                
                print(' '*gapvalue,f'M O D I F Y      D O C T O R     D E T A I L S')
                print(' '*gapvalue,f'ENTER DOCTOR-ID =',end=' ')
                u_did=int(input(' '))
                if isValid_id('doctor','did',u_did)==False:
                    pass
                else:
                    viewAllRecords_by_id('doctor','did',u_did)
                    print(' '*gapvalue,'ARE YOU SURE TO MODIFY ABOVE RECORD?')
                    print(' '*gapvalue,'PRESS N/n TO CANCEL UPDATE OPERATION=',end='')
                    ch_edit=input()
                    if ch_edit.lower()=='n':
                        print(' '*gapvalue,'\nUPDATE OPERATION ABORTED! PRESS ENTER KEY TO CONTINUE.')
                        input()
                    else:
                        print(' '*gapvalue,'UPDATE INITIATED',end='');
                        update_doct(u_did)
            
        elif(ch=='4'):
            #Delete doc
            print(' '*gapvalue,'Input ',end='');admPass=pi.pwinput()
            if not isauth_user(admPass):
                print(' '*gapvalue,'INVALID PASSWORD! PRESS ENTER KEY TO CONTINUE')
            else:
                
                print(' '*gapvalue,f'D E L E T E      D O C T O R     D E T A I L S')
                print(' '*gapvalue,f'ENTER DOCTOR-ID =',end=' ')
                u_did=int(input(' '))
                if isValid_id('doctor','did',u_did)==False:
                    pass
                else:
                    viewAllRecords_by_id('doctor','did',u_did)
                    print(' '*gapvalue,'ARE YOU SURE TO MODIFY ABOVE RECORD?')
                    print(' '*gapvalue,'PRESS N/n TO CANCEL DELETE OPERATION=',end='')
                    ch_edit=input()
                    if ch_edit.lower()=='n':
                        print(' '*gapvalue,'\DELETE OPERATION ABORTED! PRESS ENTER KEY TO CONTINUE.')
                        input()
                    else:
                        print(' '*gapvalue,'DELETE INITIATED',end='');
                        delete_record_by_id('doctor','did',u_did)
        #------------------------------------------------------------------
        elif(ch=='5'):
            #NEW PATIENT
            add_patient()
        elif (ch=='6'):
            viewAllRecords('patient')
        elif ch=='7' :
            #Modify PATIENT
            
            print(' '*gapvalue,'Input ',end='');admPass=pi.pwinput()
            if not isauth_user(admPass):
                print(' '*gapvalue,'INVALID PASSWORD! PRESS ENTER KEY TO CONTINUE')
            else:
                
                print(' '*gapvalue,f'M O D I F Y    P A .T I E N T    D E T A I L S')
                print(' '*gapvalue,f'ENTER PATIENT-ID =',end=' ')
                u_pid=int(input(' '))
                if isValid_id('patient','pid',u_pid)==False:
                    pass
                else:
                    viewAllRecords_by_id('patient','pid',u_pid)
                    print(' '*gapvalue,'ARE YOU SURE TO MODIFY ABOVE RECORD?')
                    print(' '*gapvalue,'PRESS N/n TO CANCEL UPDATE OPERATION=',end='')
                    ch_edit=input()
                    if ch_edit.lower()=='n':
                        print(' '*gapvalue,'\nUPDATE OPERATION ABORTED! PRESS ENTER KEY TO CONTINUE.')
                        input()
                    else:
                        print('\n',' '*gapvalue,'UPDATE INITIATED',end='');
                        update_patient(u_pid)

            
        elif (ch=='8'):
            #DELETE PATIENT
            print(' '*gapvalue,'Input ',end='');admPass=pi.pwinput()
            if not isauth_user(admPass):
                print(' '*gapvalue,'INVALID PASSWORD! PRESS ENTER KEY TO CONTINUE')
            else:
                
                print(' '*gapvalue,f'D E L E T E      P A T I E N T')
                print(' '*gapvalue,f'ENTER PATIENT-ID =',end=' ')
                u_pid=int(input(' '))
                if isValid_id('patient','pid',u_pid)==False:
                    pass
                else:
                    
                    viewAllRecords_by_id('patient','pid',u_pid)
                    print(' '*gapvalue,'ARE YOU SURE TO DELETE ABOVE RECORD?')
                    print(' '*gapvalue,'PRESS N/n TO CANCEL DELETE OPERATION=',end='')
                    ch_edit=input()
                    if ch_edit.lower()=='n':
                        print(' '*gapvalue,'DELETE OPERATION ABORTED! PRESS ENTER KEY TO CONTINUE.')
                        input()
                    else:
                        print(' '*gapvalue,'DELETE INITIATED',end='');
                        delete_record_by_id('patient','pid',u_pid)

        elif (ch=='9'):
            #Treatement
            print('D O C T O R    L O G I N    F O R M')
            
            print(' '*gapvalue,'INPUT DOCTOR-ID.:',end='');did=int(input())
            if doctor_Login(did)==False:
                pass
            else:
                
                viewAllRecords_by_id('patient','refer_to_dr',did)
                save_treatement(did)
        elif ch=='10':
            print(' '*gapvalue,'INPUT DOCTOR-ID.:',end='');did=int(input())
            if doctor_Login(did)==False:
                pass
            else:
                viewAllRecords_by_id('patient','refer_to_dr',did)
            
            pass
        elif ch=='11':
            #Modify emp
            print(' '*gapvalue,f'P A T I E N T     H I S T O R Y')
            print('*'*80)
            view_patient_history()
            print('*'*80)
        elif ch=='12':
                
            print(' '*gapvalue,'Thanks for using .... Press ENTER key to Exit....')
            input()
            sys.exit()

        else:
            print(' '*gapvalue,'INVALID INPUT! Kindly use option 1-9.')
#------end of start.py---------------
