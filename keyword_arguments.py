# kwargs* 

def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentinfo(name="bittu",age=24,city="Bangalore")
studentinfo(name="abhishek",age=26,city="Hyderabad")