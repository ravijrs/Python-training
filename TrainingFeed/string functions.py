# string functions
word = " pyt hon dg e ger g "
word = word.lower()
word = word.upper()
word = word.lower()
word = word.capitalize()
word = word.replace(" ", "")
word = word.count("g")
# word = word.replace(" ", "")
print(word)


word = "   this  is    python   class day 3  "
word = word.strip()
word = word.capitalize()
word = word.split()
word = "-".join(word)
word = word.replace("y", "Y")
word = word.split("-")
print(word)


"""
Expected Output: 
--------------------
This-is-pYthon-class-daY-3
"""
print()