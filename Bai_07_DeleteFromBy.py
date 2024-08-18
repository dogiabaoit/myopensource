import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount,"record(s) deleted")

sql_2 = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql_2,adr)
mydb.commit()

print(mycursor.rowcount,"record(s) deleted")