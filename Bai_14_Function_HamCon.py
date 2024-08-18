def my_function():
    print("Hello everyone")
my_function()

def my_function(name):
    print(name + " GIA BAO")
my_function("DO")
print()

def my_function(country = "Norway"):
    print("I am from "+ country)
my_function("Sweden")
my_function()
print()

def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print()

#HAM CON TRA VE GIA TRI
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
print()

#DE QUY
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)