# list [], ordered, mutable
names = []
print(f"After initializing names: {names}\n")

names.append("akash")
print(f"After appending 'akash': {names}\n")

names.append("sri vidhya")
print(f"After appending 'sri vidhya': {names}\n")

names.insert(1, "gayatri")
print(f"After inserting 'gayatri' at index 1: {names}\n")

deleted_name = names.pop()  # you can store popped element
print(f"After popping last element '{deleted_name}': {names}\n")

names.append(deleted_name)
print(f"After appending popped element '{deleted_name}': {names}\n")

names.remove("akash")
print(f"After removing 'akash': {names}\n")


names.insert(2, "mouneesh")
print(f"After inserting 'mouneesh' at index 2: {names}\n")

print(f"Last two elements: {names[-2:]}\n")

print(f"'sudhir' in names: {'sudhir' in names}\n")

names[2] = names[2].upper()
print(f"After converting index 2 to uppercase: {names}\n")

names.extend(["sudhir"])
print(f"After extending with ['sudhir']: {names}\n")

names.append(['srinu', 'anil', 'sudhir'])
print(f"After appending ['srinu', 'anil', 'sudhir']: {names}\n")

req = names[-1]
names.pop()
print(f"After popping the last list: {names}\n")

names = names + req 
print(f"After concatenating names & req: {names}\n")

print(f"List created with [0, 1]*5: {[0, 1]*5}\n")

names.sort(reverse=True)
print(f"Descending Order: {names}\n")

names.sort()
print(f"Ascending Order: {names}\n")

print(f"Sum of [1, 2, 3, 4]: {sum([1, 2, 3, 4])}\n")

name = ("CodeWala",)
print(f"List created from tuple: {list(name)}\n")

bio = ["1001", "steeve", "brooklyn"]
_id, *rest = bio
print(f"Remaining elements after unpacking bio: {rest}")