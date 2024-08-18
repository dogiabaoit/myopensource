#Tuple mot khi da duoc tao ra se khong the thay doi
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])

for x in thistuple:
    print(x)

if "apple" in thistuple:
    print("Yes, apple is in the fruits tuple")

print(len(thistuple))

del thistuple           #chi co the su dung ham del de xoa tuple

#CAU TRUC CUA TUPLE
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(thistuple.count("apple"))      #dem so luong
print(thistuple.index("banana"))     #tim kiem va tra ve vi tri