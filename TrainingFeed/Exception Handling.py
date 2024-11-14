""" 
-Exception Handling
  -try (if no error)
  -except (if error occurs)
  -finally (executes either way)
"""

try:
    numerator = int(input())
    denominator = int(input())
    print(numerator/denominator)
except Exception as e:
    print("Denominator should not be 0")
    print("ERROR: ", e)

print("=============================")

try:
    num = int(input())
    print(num)
    
except Exception as e:
    print("Please enter valid input", e)

finally:
    print("I will execute anyhow")