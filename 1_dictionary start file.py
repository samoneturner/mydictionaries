import random

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(type(phonebook))
print(len(phonebook))

mydictionary = dict(m=9, n=10)
print(mydictionary)


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

# print(phonebook["Chris"])
# print(phonebook["chris"])

name = "chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")
print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

phonebook["Chris"] = "555-0123"
phonebook["Joe"] = "555-4444"

print(phonebook)


print()
print("*****  end section 3 ********")
print()




print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]

print(phonebook)


print()
print("*****  end section 4 ********")
print()



print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()


for key in phonebook:
    print(key)
    print(phonebook[key])  # If you wanted the value instead of the key#

for v in phonebook.values():
    print(v)

for k, v in phonebook.items():
    print(f"The Key: {k} and the value: {v}")

for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print("*****  end section 5 ********")
print()



print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get(
    "Chris", "key not found"
)  # if lower case then you get key not found
print(phone)

phonebook.clear()
print(phonebook)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris", "not found")
print(remove)
print(phonebook)

print()
print("*****  end section 7 ********")
print()



print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem() #random is not working, it is only deleteing the last one in the dictionary#
print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()


"""
print()
print("*****  start section 9 - using random and converting to list ********")
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)  # only works on list#
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])


print()
print("*****  end section 9 ********")
print()
