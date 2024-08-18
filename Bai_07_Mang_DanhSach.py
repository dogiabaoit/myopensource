thisList = ["apple","banana","cherry"]
print(thisList)
print(thisList[0])
print(thisList[1])
print(thisList[2])

thisList[1] = "blackcurrant"
print(thisList)

#Vong lap qua danh sach
for x in thisList:
    print(x)

#Kiem tra neu ton tai item
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

#Chieu dai mang
print(len(thisList))

#Them vao mang
thisList.append("orange")
thisList.append("quýt")
print(thisList)
thisList.insert(1, "ổi")    #chen vao vi tri so 1
print(thisList)

#Xoa khoi mang
thisList.remove("ổi")
print(thisList)
thisList.remove(thisList[1])        #xoa theo vi tri
print(thisList)
thisList.pop()                      #xoa vi tri cuoi
print(thisList)
thisList.pop(1)                     #xoa theo vi tri
print(thisList)

thislist = ["apple", "banana", "cherry"]
del thislist[0]                     #xoa theo vi tri
print(thislist)
del thislist                        #xoa toan bo mang

thislist = ["apple", "banana", "cherry"]
thislist.clear()                    #Mang rong
print(thislist)

#Copy mang
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#CAU TRUC LIST()
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Cac cau lenh khac
thislist.append("ổi")
print(thislist)
thislist2 = thislist.copy()
print(thislist2)
thislist2.clear()
print(thislist.count("apple"))
thislist2.extend("cóc")     #Chia ky tu
print(thislist2)
thislist.reverse()          #Dao nghich danh sach
print(thislist)