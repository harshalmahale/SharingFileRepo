import mysql.connector

con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
curs = con.cursor()
curs.execute("insert into students value(104,'Kim')")
con.commit()
con.close()

print("Finished....")

