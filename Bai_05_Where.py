import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE name = 'John'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print()

#DANG TIM KIEM THEO TU KHOA
sql_2 = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql_2)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print()
#Hoac tach rieng gia tri
sql_3 = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql_3, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)