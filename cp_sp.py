cp=int(input("enter the cost price: "))
sp=int(input("enter the selling price: "))
if(sp>cp):
    gain=sp-cp
    gain_percent=gain*100/cp
    print("The gain is",gain,"and the gain percentage is",gain_percent,"%")
elif(sp<cp):
    loss=cp-sp
    loss_percent=loss*100/cp
    print("The loss is",loss,"and the loss percentage is",loss_percent,"%")
else:
    print("sp and cp are same.")
