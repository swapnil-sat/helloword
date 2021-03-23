# fact=1
# for i in range(1,6):
#     if (i==0 | i==1):
#         print("factorial is one")
#     else:
#         fact=fact*i
#         print("factorial is :",fact)

# _______________________________________________________________________________
# add = 0
# def add(n):
#     for i in range(1,n+1):
#         add = add + 1
# add(5)
# _______________________________________________________________________________
# def str_len(str):
#     if(str==''):
#         return 0
#     else:
#         return 1 + str_len (str[1:])
#
# a=str_len('Akshay')
# print(a)
# _______________________________________________________________________________
# def fun(x,y):
#     if(x==0):
#         return y
#     else:
#         return fun(x-1,x+y)
# a=fun(8,3)
# print(a)
# _______________________________________________________________________________
def fun(a,b):
    if(b==0):
        return 0
    if(b%2==0):
        return fun(a+a,b//2)
        return fun(a+a,b//2)+a
a=fun(2,3)
print(a)
