a = "Hello, World!"
print(a[1])     #in ra 1 ky tu trong a

b = "Hello, World!"
print(b[2:5])   #in ra tu ky tu thu 2 den thu 5

a = " Hello, World! "
print(a.strip()) #Su dung ham strip() de cat khoang trang thua, returns "Hello, World!"

a = "Hello, World!"
print(len(a))   #Su dung ham len() de dem chieu dai chuoi

a = "Hello, World!"
print(a.lower())    #Su dung ham lower() de chuyen doi chu thuong

a = "Hello, World!"
print(a.upper())    #Su dung ham upper() de chuyen doi chu IN HOA

a = "Hello, World!"
print(a.replace("H", "J"))  #Thay the chu H thanh chu J

a = "Hello, World!"
print(a.split(",")) # Cat thanh 2 chuoi, returns ['Hello', ' World!']
b = a.split(",")
print(b[0])
print(b[1])

#NHAP CHUOI TU BAN PHIM VA HIEN THI
print("Enter your name:")
x = input()
print("Hello, ",x)

