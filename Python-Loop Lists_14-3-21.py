# ====================================================================================||
# ||         Python- Loop Lists                                                       ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >Loop through a list
# by using a for loop.
# E.x
# print all items in the list,one by one
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# for x in thislist:
#     print(x)
# >>>Loop through the index number .
# loop through th elist items by referring to their inidex number.
# use the range() and len() function to create a suitable iterable.
# E.x
# Print all items by referring to their index number.
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# for i in range(len(thislist)):
#     print(thislist[i])
# the iterable created in the example above [0,1,2]
# >>>>.using a While loop<<<<<
# loop through the list items by using a while loop.
# use the len() function to determine the length of the list ,then start at 0 and loop your way through the list items by refering
# to their indexes.
# Remember to increase the index by 1 after each iteration.
# E.x
# print all items using a while loop to go through all the index numbers.
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1
# >>>>Loop using list comprehension .
# list comprehension offers the shortest syntax for looping through lists:
# E.x
# A short hand for loop that will print all items in a list:
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# [print(x) for x in thislist]
#                                                   *******