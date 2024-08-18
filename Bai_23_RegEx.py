import re
#Check if the string starts with "The" and ends with "Minh":
txt = "The rain in Ho Chi Minh"
x = re.search("^The.*Minh$", txt)
if (x):
    print("Yes, We have a match")
else:
    print("No match")

str = "The rain in Spain"
x = re.findall("ai", str)   #Loc tim tat ca ky tu 'ai'
print(x)
x = re.findall("Portugal", str)
print(x)

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

#Tach chuoi thanh mang
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

#Thay the chuoi
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

#Tim kiem va tra lai ket qua dang Doi tuong
str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())                 #Tim kiem va tra ve vi tri bat dau va ket thuc
print(x.string)                 #Xuat day du chuoi
print(x.group())                #Xuat ra tu vi tri tim kiem