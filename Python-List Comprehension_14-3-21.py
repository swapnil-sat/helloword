# ====================================================================================||
# ||         Python- List Comprehension                                               ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>List Comprehension<<<<<
# it offers a shorter syntax when you want to create a new list based on the values of an exisiting list.
# E.x
# Based on a list of fruits ,you want a new list,containing only the fruit with the letter "a" in the name.
# without list comprehension you will have to write a for statement with a condition test inside.
# E.x
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[]
# for x in thislist:
#     if "a" in x:
#         newlist.append(x)
#     print(newlist)
# with list comprehension you can do all that with only one line of code
# E.x
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[x for x in thislist if"a"in x]
# print(newlist)
# >>>The syntax<<<
# newlist=[expression for item in iterable if condition == True]
# the return value is a new list ,leaving the old list unchanged.
# >condition<
# a filter that only accept the items that valuate to True.
# E.x
# only accept items that are not "apple"
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[x for x in thislist if x!="apple"]
# print(newlist)
# the condition if x !="apple" will return True for all element other than "apple"making the new list contain all fruits
# except "apple"
# The condition is option and can be omitted:
# E.x
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[x for x in thislist]
# print(newlist)
# >>>Iterable<<<<
# the iterable can be any iterable object like a list ,tuple ,set etc.
# E.x
# you can use the range()function to create an iterable.
# newlist=[x for x in range(10)]
# print(newlist)
# same example ,but with a ccondition.
# Accept only numbers lower than 5:
# newlist=[x for x in range(10)if x<5]
# print(newlist)
#  >>Expression<<<<
# the expression is the current item in the iteration but it is also the outcome which you can manipulate before it ends up
# like a list item in the new list :
# E.x
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[x.upper()for x in thislist]
# print(newlist)
# E.x
# set all values in the new list to "hello"
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=['hello' for x in thislist]
# print(newlist)
# the expression can also contain conditions ,not like a filter ,but as a way to manipulate the outcome .
# E.x
# Return "orange"instead of "banana"
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# newlist=[x if x!="banana" else "orange" for x in thislist]
# print(newlist)
# the expression in the example above says :
# "return the item if it is not banana ,if it is banana returns orange
#                                               ******