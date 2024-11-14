# type conversions
""" 
- we can convert any data type into str
"""

num = (20)
print(type(num))

# int -> str
num = 30 #int
num = str(30) #str
print("int->str====", num, type(num))


# int -> float
num = 30 #int
num = float(30) #str
print("int->float====", num, type(num))

num = 40.99999
num = int(num)
print("float->int====", num, type(num))


num = "123"
num = int(num)
print("str->int====", num, type(num))

num = "123.9"
num = float(num)
print("str->float====", num, type(num))
num = "123.9"
num = float(num)
num = int(num)
print("str->int====", num, type(num))

# non-zeroes or non-empty -------> True
# zeroes or empty -------> False
value = "temp"
value = bool(value)
print("str->bool===", value, type(value))