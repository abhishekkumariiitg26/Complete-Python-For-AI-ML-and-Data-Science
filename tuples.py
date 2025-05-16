'''
ordered
immutable
duplicates allowed
any datatypes
mixed datatypes
'''
colours=("red","yellow","orange")
#unpacking of the tuple
color1,color2,color3=colours
print(color1)

my_tuple=(1,2,3,4,5,6,7,8)
list=[]
for i in reversed(my_tuple):
    print(i,end=" ")