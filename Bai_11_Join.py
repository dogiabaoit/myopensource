import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database="dogiabao"
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, \
                    name VARCHAR(255), fav INT)")
except:
    print("Da ton tai users table")
sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
        ('John', 154),
        ('Peter', 154),
        ('Amy', 155),
        ('Hannah', 0),
        ('Michael', 0)
    ]
mycursor.executemany(sql, val)
mydb.commit()
try:
    sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
    val = [
        (154, 'Chocolate Heaven'),
        (155, 'Tasty Lemons'),
        (156, 'Vanilla Dreams')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
except:
    print()

#THUC HIEN TRON HAI TABLE (khoa chinh, khoa ngoai)
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#LEFT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
#RIGHT JOIN
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"