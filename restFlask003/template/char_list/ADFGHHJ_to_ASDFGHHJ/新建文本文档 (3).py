def func(x,y):
    print(x,y)
    x=x*y
    y=y+1
    if x<1000:
        return func(x,y)
    else:
        return x
    
print(func(1,1))
# x=1
# for i in range(1,10):
#     x=x*i
# print(x)