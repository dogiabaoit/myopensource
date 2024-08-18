import mysql.connector
checked=1
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

if checked==1:
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE TABLE products (name VARCHAR(255),amount INT)")
    except:
        print("Table products da ton tai")

    try:
        mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,"  # Tao khoa chinh
                             "name VARCHAR(255),address VARCHAR(255))")
    except:
        print("Table customers da ton tai")
    #Them column trong bang
    mycursor.execute("ALTER TABLE products ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

