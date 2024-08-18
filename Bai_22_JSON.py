import json

#Vi du doan JSON sau
x = '{"name":"BAO","age":32,"city":"Ho Chi Minh"}'

#parse x:
y = json.loads(x)

#ket qua thong qua tu dien Python sau:
print(y["age"])
print()

#CONVERT TU PYTHON QUA JSON:
x = {
    "name": "Bao",
    "age": 32,
    "city": "HCM"
}
y = json.dumps(x)
print(y)
print()

#Ban co the chuyen doi cac doi tuong Python cac kieu sau thanh chuoi JSON:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print(json.dumps(x, indent=4))                          #chuyen doi co cau truc de de doc
print(json.dumps(x, indent=4, separators=(". "," = "))) #chuyen doi cau truc de doc, va chuyen doi ket thuc thanh dau '.', gan gia tri '='
print(json.dumps(x, indent=4, sort_keys=True))          #co sap xep

