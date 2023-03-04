import cx_Oracle
 

try:
 
    con = cx_Oracle.connect('Raj/admin@localhost:1521/xe')
    print(con.version)
 
   
    cursor = con.cursor()
 
   
    cursor.execute(
        "create table std123(id integer primary key, name varchar2(30))")
 
    print("Table Created successfully")
except :
    print("There is a problem with Oracle")
