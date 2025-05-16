size=int(input("Enter the size of the list: "))
print("Enter the elements of the list: ")
list=[]
for _ in range(size):
    num=int(input())
    list.append(num)
print(list)
num1=int(input("Enter the index: "))
num2=int(input("Enter another index: "))
temp=list[num1]
list[num1]=list[num2]
list[num2]=temp
print(list)