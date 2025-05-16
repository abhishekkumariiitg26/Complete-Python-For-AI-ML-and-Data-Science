# properties of dictionary

'''
ordered 
changeable
unindexed
duplicates not allowed
any datatype
'''

# making a dictionary called Phone_dictionary

Phone_directory={
    "bittu":6521452369,
    "alexwa":6262173362,
    "jaddu":1414173314,
    "ponky":987456321
}

# printing phone dictionary

print(Phone_directory)

# printing length of phone dictionary

print(len(Phone_directory))

# printing type of phone dictionary

print(type(Phone_directory))

# getting the value for jaddu

print(Phone_directory["jaddu"])
print(Phone_directory.get("jaddu"))  # do the same thing as above

# changing the values of the dictionary

Phone_directory["jaddu"]=12345678910
print(Phone_directory) 

# adding new entry
Phone_directory["Modi"]=1542698745213
print(Phone_directory)

more_phones={
    "prince":784512,
    "salman":5478,
}
Phone_directory.update(more_phones)
print(Phone_directory)

# removing the entry jaddu

Phone_directory.pop("jaddu")
print(Phone_directory)

# to remvoe last added item, we use popitem

Phone_directory.popitem()
print(Phone_directory)

# emptying the dictionary

# Phone_directory.clear()
# print(Phone_directory)

# printing keys of the dictionary

for i in Phone_directory:
    print(i,end=" ")

# printing values of the dictionary

print()
for i in Phone_directory:
    print(Phone_directory[i],end=" ")


print()
for i in Phone_directory.items():
    print(i)


print()
for i,j in Phone_directory.items():
    print(i,j)
