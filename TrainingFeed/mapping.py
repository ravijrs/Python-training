# map, filter
""" 
map(do) will store whatever function returns
filter will store whenver function returns True
"""
arr = [1, 3, -2, 1, -23, -34]

"""separating even numbers with normal code"""
positives = []
for i in range(len(arr)):
    if arr[i] > 0:
        positives.append(arr[i])
print(positives)

"""separating even numbers with filter"""
# filter(function, iterable)
print(list(filter(lambda x:x>0, arr)))



# map (function, iterable)
"""To take space separated int inputs as a list using normal code"""
data = []
arr = input("Enter nums: ").split()
for i in range(len(arr)):
    data.append(int(arr[i]))
print(data)

"""To take space separated int inputs as a list using map"""
data = list(map(int, input("Enter nums: ").split()))
print(data)


# filter with named and anonymous functions
def isPositive(n):
    return n > 0

arr = [1, 2, 3, -4, 5, -6]
print(list(filter(isPositive, arr)))
print(list(filter(lambda x:x>0, arr)))


# map with named and anonymous functions
def increase(n):
    return n+5

arr = [1, 2, 3]
print(list(map(increase, arr)))
print(list(map(lambda x:x+5, arr)))