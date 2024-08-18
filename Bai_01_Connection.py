import mysql.connector
#KET NOI CO SO DU LIEU
checked = 1
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",               #Nho vao Workbench cap quyen cho account neu co loi khi tao database
        passwd="123456"
    )
except:
    checked = 0
    print("Khong ket noi dưoc")

#TAO DATABASE
if checked==1:
    mycursor = mydb.cursor()
    #mycursor.execute("SHOW DATABASES")
    #for x in mycursor:
    #   print(x)
    try:
        mycursor.execute("CREATE DATABASE dogiabao")
    except:
        print("Tai khoan 'dogiabao' da ton tai")

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        passwd="123456",
        database="dogiabao"       #Them ket noi csdl
    )
except:
    checked = 0
    print("Khong ket noi dưoc")

#Dong CSDL
mydb.close()