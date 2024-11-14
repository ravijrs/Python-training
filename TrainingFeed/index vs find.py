# index vs find

sentence = "this is zkdgber ger grt zach salvatore"
# print(sentence.index("j"))
# print(sentence.rfind("z"))
print(sentence.find("j"))


sentence = "steewefrgkj@nrjkrhtgrejkrhrve@ gmail.com"
print(sentence[sentence.rfind("@"):] == "@gmail.com")

print(sentence.startswith("T"))
print(sentence.endswith("@gmail.com"))

sentence = "1223"
print(sentence.isalnum())
print(sentence.isalpha())
print(sentence.isdigit())