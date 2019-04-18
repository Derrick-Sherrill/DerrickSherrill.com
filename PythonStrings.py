A = "strings, STRINGS, and more strings!   "


print(A.capitalize())
print(A.lower())
print(A.upper())
print(A.title())

new_phrase = A.replace("STRINGS","strings")
print(new_phrase)

print(new_phrase.count("strings"))
print(new_phrase.find("more",10,30))

ListA = ['3','2','1']
Join_symbol = ' -'
Joined_string = Join_symbol.join(ListA)
print(Joined_string)

split_joined_string = Joined_string.split(' -')
print(split_joined_string)

print("Hello\t from\n me!")
