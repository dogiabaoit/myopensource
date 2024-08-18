#Tap hop la bo KHONG CO THU TU va KHONG DUOC CHI DINH.
#Tap hop se khong duoc thay doi, nhung them duoc item moi
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
    print(x)
print("")

#Them vao tap hop
print("apple" in thisset)
thisset.add("ổi")
print(thisset)
thisset.update(["orange","mango","grapes"])
print(thisset)
print("")

print(len(thisset))
print("")

#Xoa item
thisset.remove("ổi")
print(thisset)
thisset.discard("banana")
print(thisset)
thisset.pop()
print(thisset)
thisset.clear()         #Empty toan bo tap hop
del thisset
print("")

#Cau truc cua set()
thisset = set(("apple","banana","cherry"))
print(thisset)

#Cac lenh khac
thisset2 = set(("apple","orange","cherry"))
print(thisset.difference(thisset2))         #tra ve tap hop cac phan tu khac tap hop thu 2
thisset2.difference_update(thisset)         #xoa tap hop cac phan tu cung co trong tap hop thu 2
print(thisset)
print(thisset2)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)                       #Loc phan tu co trong ca tap x va y
print(z)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)                    #Xoa cac phan tu khong co trong tap y
print(x)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)                         #Kiem tra khong co phan tu nao cua tap x co trong tap y
print(z)
print("")

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)                           #Kiem tra tap x co phai la tap con cua tap y
print(z)
print("")

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)                         #Kiem tra tap x co phai la tap cha cua tap y
print(z)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)               #Tron cac phan tu khac nhau tu hai tap hop
print(z)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)            #Tron cac phan tu khac tu tap y vao tap x, xoa phan tu giong nhau
print(x)
print("")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}        #Tron tat ca cac phan tu ke ca phan tu giong nhau
z = x.union(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)