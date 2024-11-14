"""  
Create empty list 'names' and Get n inputs from the user & store it in 'names'
After taking n inputs, 
	convert even indexed words into upper and odd indexed words to lower

finally, form a sentence with all the modified words into one sentence separated by -
print the list after modified
print the combined sentence separated with -

Sample Input1:
  ["Alaric", "SteFan", "Damon", "ElEna"]
Sample Output1:
  ["ALARIC", "stefan", "DAMON", "elena"]
  ALARIC-stefan-DAMON-elena

Sample Input2:
  ["Chris", "Evans", "Steeve", "CodeWala"]
Sample Output2:
  ["CHRIS", "evans", "STEEVE", "codewala"]
  CHRIS-evans-STEEVE-codewala

Sample Input3:
  ["Caroline", "KlaUs"]
Sample Output3:
  ["CAROLINE", "klaus"]
  CAROLINE-klaus

CONSTRAINTS:
  words can have upper/lower/digits in it 

"""
names = []
for i in range(5):
    user = input()
    names.append(user)
for i in range(5):
    if i%2 == 0:
        names[i] = names[i].upper()
    else:
        names[i] = names[i].lower()
print(names)
print("-".join(names))
