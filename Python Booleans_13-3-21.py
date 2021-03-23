# ====================================================================================||
# ||         Python - Booleans                                                        ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>>>Python Booleans <<<<<<<<
# Booleans represents one of two values: True or False.
# you need to know if an expression is True or False.
# You can evaluate any expression in python and get one of two answers True or False.
# When you compare two values the expression is evaluated and pyhton returns the Boolen answer.
# E.g
# print(10>9)
# print(10==9)
# print(10<9)
# ______________________________________________________________________________________________________________________
# E.g
# Print a message based on whether the condition is True or False.
# a=200
# b=33
# if b>200:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
# ______________________________________________________________________________________________________________________
# >>>>Evaluate valued and variables.
# the bool() function allows you to evaluate any value ,and give you True or False in return,
# E.g
# Evaluate a string and a number.
# print(bool("hello"))
# print(bool(15))
# ______________________________________________________________________________________________________________________
# >>>>Most values are True.
# any value is evaluated to True if it has some sort of content.
# >Any string is True,except empty string .
# >Any number is True ,except 0.
# >Any list,tuple ,set and dictionary are True ,except empty ones.
# E.g
# print(bool("abc"))
# print(bool())
# print(bool(123))
# print(bool(["apple","Cherry","banana"]))
# ______________________________________________________________________________________________________________________
# >>>Some values are false.
# in fact there are not many values that evaluate to false except empty values such as (),{},[] ,"",the number 0 and the value None and of cource the value
# False evaluates to False.
# E.g
# the folloiwng will return False.
# a=bool(False)
# b=bool(None)
# c=bool(0)
# d=bool("")
# e=bool(())
# f=bool({})
# g=bool([])
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# ______________________________________________________________________________________________________________________
# One or more value,oro object in this case evaluates to False and that is if you have an object that is made from a class
# with a __len__ function that returns 0 or False.
# E.g
# class myclass():
#     def __len__(self):
#         return 0
# myobj=myclass()
# print(bool(myobj))
# ______________________________________________________________________________________________________________________
# >>>Function can Return a Boolen.
# you can create function that returns a Boolean value:
# E.g
# Print the answer of a function .
# def myfunction():
#     return True
# print(myfunction())
# you can execute caode based on the Boolean Answer of a function.
# E.g
# Print"YES" if the function returns True,otherwisw print"No".
# def myfunction():
#     return True
# if myfunction():
#     print("YES!")
# else:
#     print("No!")
# ______________________________________________________________________________________________________________________
# Python also has many built -in function that returns a Boolean value ,like the isinstance() function which can be used
# to determine if an object is pf a certain data type>
# E.g
# Check if an object is an integer or not.
# x=200
# print(isinstance(x,int))
#                                                   ***