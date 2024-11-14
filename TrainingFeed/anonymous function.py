# lambda  -> anonymous function
def wish(name):
    return f"Hey {name}, Happy Coding"
print(wish("stefan"))
print(wish("damon"))

wishing = lambda name:f"Hey {name}, Happy Coding"
print(wishing("stefan"))
print(wishing("damon"))


def addition(n1, n2):
    return n1 + n2
print(addition(10, 20))

addition = lambda n1, n2: n1 + n2
print(addition(10, 20))


name = "elena"
def homepage():
    global name
    name = "caroline"
homepage()
print(name)


name = "elena"
def homepage():
    global name
    name = "caroline"
homepage()
print(name)


res = 1
for i in range(1, 6):
    res = res * i
print(res)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
""" 
n = 5
5 * fact(4)
     |--4 * fact(3)
             |--3 * fact(2)
                      |--2 * fact(1) => base case



def fib(n):
    if n == 0:
        return 0
    if n ==  1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(4))
explanation = """ 
	n = 4
	fib(3)
		|-- fib(2)
			|-----fib(1)  => base case
					fib(0)  => base case
			fib(1)
	fib(2)
		|-- fib(1) => base case
			fib(0) => base case 
	"""
print(explanation)


# yield
def nums1(n):
    for i in range(n):
    	return i
print(nums1(5))

def nums2(n):
    for i in range(n):
    	yield i
print(tuple(nums2(5)))