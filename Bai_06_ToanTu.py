x = 13
y = 6
print(x+y)
print(x-y)
print(x*y)
print(x/y)      #Chia lay ca so le
print(x%y)      #Chia lay du
x = 3
y = 2
print(x**y)     #Luy thua
x = 13
y = 6
print(x//y)     #Chia lay nguyen
print("")

#PHEP TOAN GAN
x = 10
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x = 10
x //= 3
print(x)
x **= 3
print(x)
x = 5
x &= 3          #bit AND
print(x)
x = 5
x |= 3          #bit OR
print(x)
x ^= 3          #bit XOR
print(x)
x >>= 3         #bit dich phai
print(x)
x = 5
x <<= 3         #bit dich trai
print(x)
x = 5
print(~x)       #bit NOT
print("")

#PHEP TOAN SO SANH
x = 12
y = 11
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print("")

#PHEP TPOAN LUAN LY
x = 5
print(x > 3 and x < 10)
print(x <5 or x < 4)
print(not(x > 3 and x < 10))
print("")

#PHEP TOAN NHAN DANG
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have thew same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print("")

#PHEP TOAN THANH PHAN
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
