#HOSPITAL MGMT
import pymysql as pm
dbase='hospital_db'
#=============================================
def setup_database():
    try:
        qry_db1=f'DROP DATABASE IF EXISTS {dbase}'
        qry_db2=f'CREATE DATABASE IF NOT EXISTS {dbase}'
        con=pm.connect(user='root',password='root',host='localhost')
        print('Connection Successful')
        cur=con.cursor()
        cur.execute(qry_db1)
        cur.execute(qry_db2)
        print(f'DATABASE [{dbase}] Created Successfully')

        
    except pm.DatabaseError as e:
        con.rollback()
        print(e)
    finally:
            if cur is not None:
                cur.close()
            if con is not None:
                con.close()
#=====================================================================
def setup_tables():
    try:
        
        con=pm.connect(user='root',password='root',host='localhost',db=dbase)
        
        qry_db='CREATE DATABASE IF NOT EXISTS hospital_db'
        cur=con.cursor()
        cur.execute(qry_db)
        
        qry_doc="CREATE TABLE IF NOT EXISTS doctor( did INT primary key,dfname VARCHAR(30),dlname VARCHAR(30),gender varchar(6),password varchar(30),\
speciality varchar(40),shift varchar(10),mob varchar(12) );"
        cur=con.cursor()
        cur.execute(qry_doc)
        print('Table [doctor] Created Successfully')

        qry_patient="""CREATE TABLE IF NOT EXISTS PATIENT
                    (pid INT primary key,
                     pfname VARCHAR(30),
                     plname VARCHAR(30),
                     gender varchar(6),
                     city varchar(20),
                     age int,
                     doa date,
                     mob varchar(12),
                     refer_to_dr int,
                     symptom varchar(45),
                     consult_fee float 
                    )"""
        cur=con.cursor()
        cur.execute(qry_patient)
        print('Table [patient] Created Successfully')

        qry_treatement="""CREATE TABLE IF NOT EXISTS treatement
                    (tno INT primary key,pid INT,did INT,disease_caused_by varchar(40),
                    symptoms varchar(40),treatement_detail varchar(40),
                    prescribe_medicine varchar(50),
                    dose varchar(20),
                    no_of_days int
                    
                    )"""
        cur=con.cursor()
        cur.execute(qry_treatement)
        print('Table [treatement] Created Successfully')

        
    except pm.DatabaseError as e:
        con.rollback()
        print('Something Wrong:=>',e)
    finally:
        if cur is not None:
                cur.close()
        if con is not None:
                con.close()

#==============================================================================
def saveData():
    try:
        con=pm.connect(user='root',password='root',host='localhost',db=dbase)
        qry_doc="""
            INSERT INTO DOCTOR VALUES(101,'AMIT','KUMAR','M','1234','SURGEON-ENT','DAY','9078435952'),
            (102,'Riya','Chauhan','F','1234','Child Specialist','DAY','9078477966'),
            (103,'Neha','Awasthi','F','1234','Eye Specialist','DAY','9958070900'),
            (104,'Anurag','Sharma','M','1234','Physician','NIGHT','9971524066')
            """
        cur=con.cursor()
        cur.execute("DELETE FROM doctor")
        con.commit()
        
        cur=con.cursor()
        cur.execute(qry_doc)
        con.commit()
        print('DOCTORS DATA Generated ')
        
        
        qry_pat="""
            INSERT INTO PATIENT VALUES
            (1,'Aniket','Saraf','M','Kolkata',19,'2022-02-15','9674825476',101,'Cold Cough',500),
            (2,'amrita','Kumari','F','Lucknow',26,'2022-02-17','8895563214',103,'Eye Swelling & burning sensation',500),
            (3,'Ravi','chandra','M','kanpur',12,'2022-03-06','8090108245',102,'dysantry & vomitting',500),
            (4,'alvina','parveen','F','mahoba',39,'2021-03-20','9991588630',103,'Burning Senation & vision Problem',500),
            (5,'Zaid','Ahmad','M','Atarra',6,'2022-03-06','70551508245',102,'Fever',500),
            (6,'Zubin','shahid','f','Banda',21,'2022-03-06','8090108245',104,'Stomach Ache & Gastric ',500)
            """
        cur=con.cursor()
        cur.execute("DELETE FROM PATIENT")
        con.commit()
        
        cur=con.cursor()
        cur.execute(qry_pat)
        con.commit()
        print('PATIENT DATA Generated ')
        '''
            qry_disease="""CREATE TABLE IF NOT EXISTS treatement
                    (tno INT primary key,
                    pid INT,
                    did INT,
                    disease_caused_by varchar(40),
                    symptoms varchar(40),
                    treatement_detail varchar(40),
                    prescribe_medicine varchar(50)
                    )"""
        '''
        qry_treate="""
            INSERT INTO treatement VALUES
            (1,1,101,'VIRUS','Sore Throat Nose Running','Antibiotics & Use Luke warm Water','DOLO 500mg Paracetamol','OD',3),
            (2,2,103,'Bacteria','Eye Swelling & burning sensation','Eye Drops Multivitamin Caps Protect Eyes','ITONE','TWICE A DAY',15),
            (3,3,102,'Bacteria','dysantry & vomitting','Use boiled water & Antibiotics','abc medicine 500mg','Three times a day',3),
            (4,4,103,'Bacteria','Eye Swelling & burning sensation','Eye Drops Multivitamin Caps Protect Eyes','Just Tears','TWICE A DAY',15),
            (5,5,102,'VIRUS','Sore Throat Nose Running','Antibiotics & Use Luke warm Water','DOLO 500mg Paracetamol','Three times a day',5),
            (6,6,104,'VIRUS','Fever','Antibiotics','DOLO 500mg Paracetamol','OD',5)
            """
        cur=con.cursor()
        cur.execute("DELETE FROM treatement")
        con.commit()
        
        cur=con.cursor()
        cur.execute(qry_treate)
        con.commit()
        print('TREATEMENT DATA Generated ')
    except pm.DatabaseError as e:
        con.rollback()
        print('Something Wrong:=>',e)
    finally:
        if cur is not None:
                cur.close()
        if con is not None:
                con.close()

setup_database()
setup_tables()
saveData()
