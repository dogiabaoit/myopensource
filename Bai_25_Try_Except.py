#Try co gang bat su kien ngay ca truong hop loi xay ra neu co se duoc bo qua, han che gay loi chuong trinh
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print()

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print()

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

#Lam viec voi tap tin
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
