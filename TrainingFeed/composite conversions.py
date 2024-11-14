# composite type conversions
arr = [1, 2, 3, 3]
arr_tuple = tuple(arr)
print("list->tuple====", arr_tuple, type(arr_tuple))

arr_set = set(arr)
print("list->set====", arr_set, type(arr_set))

temp = [("name","srikanth"), ["course", "python"]]
arr_dict = dict(temp)
print("list->dict====", arr_dict, type(arr_dict))