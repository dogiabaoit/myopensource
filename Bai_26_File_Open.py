f = open("demofile.txt","wt")   #Cho phep ghi
f.write("Hello Bao\n")
f.write("I am from Ho Chi Minh city")
f.close()

#DOC FILE
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
f2 = open("demofile.txt", "rt") #Chi cho phep doc
print(f2.read())
f2.close()
print()

f3 = open("demofile.txt", "r")
print(f3.read(3))       #Chi doc 3 ky tu dau
f3.close()
print()

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()
print()

f = open("demofile.txt", "r")
for x in f:
    print(x)
f.close()

#GHI FILE HOAC TAO FILE MOI
f = open("demofile2.txt", "a")      #Se noi vao cuoi tep neu file ton tai
f.write("Now the file has more content!")
f.close()

f = open("demofile3.txt", "w")      #Se luu noi dung de len noi dung cu neu file ton tai
f.write("Woops! I have deleted the content!")
f.close()

try:
    f = open("myfile.txt", "x")     #Tao file moi, bao loi neu file da ton tai
except:
    print("File da ton tai")
finally:
    f.close()

#XOA FILE
import os
print("Ban co muon xoa file demofile.txt (Y/N)?: ")
x = input()
if x=="Y":
    if os.path.exists("demofile.txt"):  #Kiem tra xem file co ton tai khong
        os.remove("demofile.txt")
    else:
        print("The file does not exist")
else:
    print("Ban lua chon Khong xoa file demofile.txt")

#Tao Folder
os.mkdir("myfolder")
#Xoa Folder
print("Ban co muon xoa Folder 'myfolder' (Y/N)?: ")
x = input()
if x=="Y":
    os.rmdir("myfolder")
else:
    print("Ban lua chon Khong xoa folder 'myfolder'")