# ====================================================================================||
# ||         Python Global variables                                                  ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >Global variables
# variables that are created outside of a fuction (as in all of the examples above) are known as global variables.
# it is used by everyone,both inside of function and outside.
# E.g
# Create a variable outside of a function and use it inside the function .
# x="awesome"
# def myfunc():
#     print("python is " +x)
# myfunc()
# ______________________________________________________________________________________________________________________
# you create a variable with the same name inside a function this variable will be local,and can only be used inside the function .
# the global variable with the same name will remian as it was global and with the original value.
# >Create a variable inside a function with the same name as the global variable.
# x="Awesome"
# def myfunc():
#     x="fantastic"
#     print("Python is "+x)
# myfunc()
# print("python is "+x)
# ______________________________________________________________________________________________________________________
# >The Global keyword
# you create variable inside a function that variable is local and can only be used inside that function.
# to create a global variable inside a function you can use global Keyword.
# E.g
# if you use the global keyword the variable belongs to the global scope:
# def myfunc():
#     global x
#     x="fantastic"
# myfunc()
# print("python is "+x)
# also use the global keyword if you want to change a global variable inside function.
# E.g
# >to change the value of a global variable inside a function refer to the variable  by using the global keyword:
# global keyword:
# x="Awesome"
# def myfunc():
#     global x
#     x="fantastic"
# myfunc()
# print("Python is "+x)
# ______________________________________________________________________________________________________________________
