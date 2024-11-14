operators
  Arithematic ---> +, -, *, /, //, %, **
  Short hand assignment ---> +=, -=, *=, /=, //=, %=, **=
  Relational ---> <=, >=, ==, !=
  Logical    ----> and, or
  MemberShip ----> in, not in
  Identity   ----> is, is not (based on id)
"""
num = 30
num += 5 # num = num + 5
num *= 5 # num = num * 5
num /= 5 # num = num / 5

# should be greater than 20 and even number
num = 4
print((num>20) and (num%2==0))
print((num>20) or (num%2==0))

# in, not in
print("code" in "codewala")
print("code" in "Codewala")
print("code" not in "Codewala")