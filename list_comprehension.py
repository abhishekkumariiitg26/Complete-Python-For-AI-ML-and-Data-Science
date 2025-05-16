old_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[i for i in old_list if i%2==0]
print(new_list)

#copying the list
new_copied_list=new_list.copy()
print(new_copied_list)
new_copied_list=old_list+new_copied_list
print(new_copied_list)

