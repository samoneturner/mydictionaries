person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(
    person
)  # if the key exists then the value gets updated, it it does not exist then it gets appended

# print out the name of the second child
mylist = person["children"]
print(type(mylist))
print(person["children"][1])


# print out the name of the cat
print(person["pets"]["cat"])

# use a loop to print out the name of each child
for key in person["children"]:
    print(key)

# use a loop to print out the pest in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for key, value in person["pets"].items():
    print(f"the type of pet is: {key} and the name of the pet is: {value}")
