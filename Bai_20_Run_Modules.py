import Bai_20_Modules

Bai_20_Modules.greeting("Do Gia Bao")
a = Bai_20_Modules.person1["age"]
print(a)
print()

#Dinh danh Module
import Bai_20_Modules as mx
a = mx.person1["name"]
print(a)
print()

#Goi nhieu module san co khac
import platform
x = platform.system()
print(x)
print()

x = dir(platform)
print(x)
print()

#Import only the person1 dictionary from the module:
from Bai_20_Modules import person1
print(person1["age"])