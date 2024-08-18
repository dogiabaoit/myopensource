import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()

#Sap xep theo thu tu
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print()

#Sap xep giam dan
sql_2 = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql_2)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)