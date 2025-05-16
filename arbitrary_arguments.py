# any number of arguments can be passed and 
# args will be a tuple
# arbitrary arguments

def sum_all_numbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

output=sum_all_numbers(1,2,3,4,5)
print(output)