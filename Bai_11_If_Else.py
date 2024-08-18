a = 33
b = 100
if a < b:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Tap dieu kien ngan
if a > b: print("a is greater than b")
print("a") if a > b else print("b")
print("a") if a > b else print("=") if a == b else print("b")
print("")

#Ket hop toan tu luan ly
a = 8
b = 7
c = 10
if a > b and c > a:
    print("Both conditions are true")
if a > b or a > c:
    print("At least one of the conditions is true")
    