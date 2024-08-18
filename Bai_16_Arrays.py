cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[0])
print(len(cars))
print()

for x in cars:
    print(x)

cars.append("Honda")        #Them phan tu trong mang
print(cars)

cars.pop(1)                 #Xoa phan tu mang tai vi tri so 1
print(cars)
cars.remove("Honda")

cars.extend(["Honda","Toyota"]) #Them nhieu phan tu mang
print(cars)

cars.reverse()              #Dao nghich vi tri cac phan tu mang
print(cars)

cars.sort()                 #Sap xep thu tu cac phan tu trong mang
print(cars)

print(cars.index("Honda"))  #Tra ve vi tri cua phan tu trong mang

cars_2 = cars.copy()        #Copy mang
print(cars_2)

del cars_2                  Xoa mang, mang khong ton tai khi dung lenh nay
