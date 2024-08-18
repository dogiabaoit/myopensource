#Tu dien cung la mot tap hop cung khong co thu tu, nhung co the thay doi va lap chi muc
#Trong tu dien Python duoc viet voi dau ngoac nhon va chung co cac khoa va gia tri
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")

#Thay doi gia tri
thisdict["year"] = 1987
print(thisdict)

#Vong lap tung item trong tu dien
for x in thisdict:
    print(x + ": " + str(thisdict[x]))

for x in thisdict.keys():
    print(x)
print("")

for x in thisdict.values():
    print(x)
print("")

for x, y in thisdict.items():           #Lay ca key va gia tri
    print(x, y)
print("")

#Kiem tra co ton tai khong
if "model" in thisdict:
    print(thisdict.get("model"))

print(len(thisdict))
print("")

#Them phan tu
thisdict["color"] = "red"
print(thisdict)

#Xoa phan tu
thisdict.pop("model")
print(thisdict)

thisdict.popitem()      #Xoa phan tu cuoi cung
print(thisdict)
del thisdict["year"]
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict            #Xoa toan bo va se khong ton tai tap hop nay
print("")

#Copy tu dien
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict2 = dict(thisdict)
print(mydict2)
print("")

#CAU TRUC CUA TAP HOP TU DIEN
thisdict = dict(brand = "Ford", model = "Mustang", year = 1964)
print(thisdict)
print("")

#Cac tap lenh khac
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
x = car.setdefault("color", "white")
print(x)
print(car)