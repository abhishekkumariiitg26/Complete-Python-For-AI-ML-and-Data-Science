# example of set

set={"abhishek","bittu",5,45.32,8+6j,None,True,}

# properties of set

'''
unordered
immutable
unindexed
duplicates not allowed
any datatype
mix of different datatypes
'''

# printing the set

print(set)

# printing the length of the set

print(len(set))

# printitng the type of the set

print(type(set))

# traversing each element of the set using for loop

for i in set:
    print(i,end=" ")


# checking if bittu word is present in the set or not

if "bittu" in set:
    print("\nBittu is present in set.")


# adding computer to the set

set.add("computer")

# again printing the set
print(set)

# making a new set called new_set and including ram and sita in it
new_set={"ram","sita"}

# updating the old set with new set so that ram and sita will be added to our old set

set.update(new_set)

print(set)

# removing abhishek from the set

set.remove("abhishek")

# set.remove("birla") gives error since it is not present in the set
set.discard("birla")  #not give any error

# making two new sets s1 and s2
s1={'a','b','c'}
s2={'d','a','f'}

# making a new set s3 and putting values of s1 and s2 in union to it
s3=s1.union(s2)
print(s3)

# putting values of s2 in s1 and printing s1
s1.update(s2)
print(s1)

# getting insertion or common values 

s10={'a','b','c'}
s20={'d','a','f'}

s10.intersection_update(s20)
print(s10)

# getting symmetric difference of two sets
s100={'a','b','c'}
s200={'d','a','f'}

s100.symmetric_difference_update(s200)
print(s100)