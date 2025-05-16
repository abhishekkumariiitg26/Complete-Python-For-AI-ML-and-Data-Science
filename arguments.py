# default arguments



# positional argument

def get_add_values(x,y):
    print("x=",x)
    print("y=",y)
    sum=x+y
    return sum

a=9
b=8
print(get_add_values(a,b))

# keyword argument or named argument
print(get_add_values(y=9,x=7))


# default argument
print("default argument")
def get_product_values(x,y=5):
    print("x=",x)
    print("y=",y)
    product=x*y
    return product

print(get_product_values(8))

