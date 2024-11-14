""" 
-comprehensions
  -list comprehension
  -tuple comprehension
  -set comprehension
  -dictionary comprehension
"""
arr = []
n = 11
for i in range(1, n):
    arr.append(i)
print(arr)

print([i for i  in range(1, 11)]) #list comrehension
print(tuple(i for i  in range(1, 11))) #tuple comprehension
print({i for i in range(1, 11)}) #set comprehension
print({i:True  for i in range(1, 11)}) #dictionary comprehension