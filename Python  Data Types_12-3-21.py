# ====================================================================================||
# ||         Python Data Types                                                        ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >Built -in Data types
# variables can store data of different types,and different types can do different things
# python has folloiwng data types
# ______________________________________________________________________________________________________________________
# Text type                                                         str
# 1. Numeric types>             int,float,complex
# 2.sequence types>             list,tuple,range
# 3.mapping types>              dict
# 4.set types>                  set,frozenset
# 5.Boolen type>                bool
# 6.Binary types>               bytes,byterray,memoryview
# ______________________________________________________________________________________________________________________
# >Getting the data type
# the data type of any object by using the type() function:
# Example
# >Print the data type of the variable x:
# x=5
# print(type(x))
# ______________________________________________________________________________________________________________________
# >Setteing the data type
# the data type is set when you assign a value to a variable.
# Example
# 1.x="Hello World"
# 2.x=20
# 3.x=20.5
# 4.x=1j
# 5.x=["apple","Banana","Cherry"]
# 6.x=("apple","Banana","Cherry")
# 7.x=range(6)
# 8.x={"name":"John","age":36}
# 9.x=frozenset({"apple","banana","Cherry"}).
# 10.x=True
# 11.x=b"Hello"
# 12.x=bytearray(5)
# 13.x=memoryview(bytes(5))
# ______________________________________________________________________________________________________________________
# >Setting the specific Data type.
# if you want to specify the data type you can use the following constuctor
# function.
# Example.
# x=str("Hello world")
# x=int(20)
# x=float(20.7)
# x=complex(1j)
# x=list(("apple","Banana","Cherry"))
# x=tuple(("apple","Banana","Cherry"))
# x=range(6)
# x=dict("name=swapnil","age=31")
# x=set(("apple","Banana","Cherry"))
# x=frozenset(("apple","Banana","Cherry"))
# x=bool(5)
# x=bytes(5)
# x=bytearray(5)
# x=memoryview(bytes(5))
#                                               ***