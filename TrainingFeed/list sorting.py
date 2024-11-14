name = "hello"
for letter in range(len(name)):
    print(name[letter])
print(f"Each letter in 'hello' is printed one by one.\n")

for idx, letter in enumerate(name):
    print(idx, letter)
print(f"Each letter in 'hello' is printed with its index.\n")

nums = [2, 1, 4, 3, 5]
nums.sort(reverse=True)
print(f"List sorted in reverse order without storing : {nums}")

nums = sorted(nums)
print(f"List sorted in ascending order with storing: {nums}\n")

arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
print(f"[{arr1} == {arr2}] -> {arr1 == arr2}")  # --> True
print(f"[{arr1} is {arr2}] -> {arr1 is arr2}")  # --> False (because it will compare id's)

nums1 = [1, 2, 3, 4]
nums2 = nums1 #it is not copying the list, just referencing
nums2.append(5)
print(f"nums1 after appending 5 through nums2: {nums1}")

nums3 = nums1.copy() #it is copying the list
nums3.append(6)
print(f"nums1 after appending 6 to a copy: {nums1}")

arr = [[1, "steeve", 40000], [2, "tony", 30000, [3, "pepper", 10000]]]
print(f"The salary of {arr[1][3][1]} is {arr[1][3][2]}.")