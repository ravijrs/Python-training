# *args
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")

print(numbers(10, 20, 30, 40))
numbers(30, 40)

# **kwargs(variable keyword arguments)

"""
ORDER:
   positional, Default
  	    *args, **kwargs
"""

def details(**kwargs):
    print(kwargs)

details(age=15, name="gayathri", brother="vidhya")

print("--------------------------------------------")

def details(a, **kwargs):
    print(kwargs)

details(100, age=15, name="latha", brother="maaz") 

print("--------------------------------------------")

def details(a, *args, **kwargs):
    print(a, args, kwargs)

details(100, 200, 300, 400, city="newJersey", age=15, name="asma", brother="rayyan") 