import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()

#CHI XUAT TOI DA 5 RECORD
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()

#XUAT TOI DA 5 RECORD, NHUNG BAT DAU TU VI TRI THU 3
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
