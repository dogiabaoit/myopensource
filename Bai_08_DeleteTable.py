import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()

#sql = "DROP TABLE customers"
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
