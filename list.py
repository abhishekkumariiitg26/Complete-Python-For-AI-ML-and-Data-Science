list=["fruits","veg","chicken","fish",2541,56.2145,True,8+98j,None]
for i in list:
    print(i,end=" ")
print("\n")
print(list[2])  # 0 based indexing
print(list[-2])
print(list[1:5:2])
'''
indexed based
ordered
mutable
duplicates allowed
any datatype
mixed datatypes
'''
print(type(list))
print(type(list[5]))
print(type(list[6]))
print(type(list[7]))
print(type(list[8]))

# print(type(list[9])) not available

print(len(list))  #length of list

if "veg" in list:
    print("veg is a part of the list")
if "chowmin" not in list:
    print("chowmin is not in list")


'''
append
insert
extends

'''
print("-------------------------------------------------------------")
list2=["puttu","prince","abhi","pagla"]
list.append("bitturaja")
print(list)
list.insert(10,"rajaji")
print(list)
list.extend(list2)
print(list)
list.remove("chicken")
list.pop()
print(list)
list.pop(0)
print(list)
list[6]="something"
print(list)
list[2:4]=["number","floating number"]
print(list)
number_list=[5,8,4,3,2,1]
number_list.sort() #works with relatable datatypes
print(number_list)
number_list.sort(reverse=True) #works with relatable datatypes in reverse order
print(number_list)