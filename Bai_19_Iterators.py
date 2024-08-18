#Kieu lap di lap lai, chay buoc tung phan tu theo tung dong lenh

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print()

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print()

mytuple = ("apple", "banana", "cherry")     #mang theo Tuple
for x in mytuple:
    print(x)
mystr = "banana"
for x in mystr:
    print(x)

#XAY DUNG LOP, DOI TUONG
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()

#DIEM DUNG
class YourNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration         #neu khong co lenh nay vong lap se chay mai

yclass = YourNumbers()
yiter = iter(yclass)
for x in yiter:
    print(x)

