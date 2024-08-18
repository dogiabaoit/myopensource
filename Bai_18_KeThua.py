class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#XAY DUNG CLASS CON
class Student(Person):
    pass                    #Thua ke

y = Student("Mike", "Olsen")
y.printname()

#Ham con ke thua tu class cha nen su dung duoc con thuoc tinh, cac ham tu class cha
class Enginneer(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.lastname, self.firstname, "to the class of", self.graduationyear)

x = Enginneer("Gia Bao", "Do", 2019)
x.welcome()
