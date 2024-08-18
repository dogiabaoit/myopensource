import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")

sql_2 = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345","Canyon 123")
mycursor.execute(sql_2,val)
mydb.commit()

print(mycursor.rowcount,"record(s) affected")