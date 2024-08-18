import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
#mycursor.execute("SELECT name, address FROM customers")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)

#Neu ban chi them mot row trong table, ban chi su dung phuong thuc fetchone()
myresult_2=mycursor.fetchone()
print(myresult_2)