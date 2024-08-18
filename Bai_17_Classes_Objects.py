class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
print()

#Ham khoi tao
class Person:
    def __init__(self, name, age):      #self giong this
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print()
p1.myfunc()
print()

#Su dung mysillyobject and abc thay vi dung 'self'
class Person_2:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p2 = Person_2("BAO", 32)
p2.myfunc()
p2.age = 33         #Modify gia tri thuoc tinh
print(p2.age)
del p2.age          #Xoa thuoc tinh cua doi tuong

del p2              #Xoa doi tuong de khoi tao lai doi tuong khac



