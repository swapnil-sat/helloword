# ====================================================================================||
# ||         Slicing                                                                  ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>Slicing<<<<<<
# you can return a range of characters by using the slice syntax.
# specify the start index ,seperated by a colon,to return a part of a string
# E.g
# get the characters from position 2 to position 5(not included:)
# b="Hello world!!"
# print(b[2:5])
# ______________________________________________________________________________________________________________________
# >>>Slice from the start<<<<<<<<
# By leaving out the start index ,the range will start at the first character.
# E.g
# get the characters from the start to position 5 (not included):
# b="Hello world!"
# print(b[:5])
# ______________________________________________________________________________________________________________________
# >>>Slice to the End<<<<<
# By leaving out the end index ,the range will go to the end.
# E.g
# Get the characters from position 2 and all  the way to the end:
# b="Hello World!"
# print(b[2: ])
# ______________________________________________________________________________________________________________________
# >>>>Negetive index<<<<<<
# use negative indexes to start the slice from the end of the string
# E.g
# Get the characters from:"o" in "World"(position-5)to,but not included:"d" in "World"
b="Hello World!"
print(b[-5:-2])
#                                                       ***