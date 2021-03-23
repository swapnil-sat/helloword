# ====================================================================================||
# ||         Python- Sort lists                                                       ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>sort list alphanumerically
# sort() method that will sort the list alphanumerically ascending by default,
# E.x
# sort the list alphabetically.
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# thislist.sort()
# print(thislist)
# >Sort the numerically.
# thislist=[9,8,56,34,2,5,77,40,30,12]
# thislist.sort()
# print(thislist)
# >>>Sort Descending
# to sort descending use the keyword argument.
# >reverse=True:
# E.x
# sort the list descending
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# thislist.sort(reverse=True)
# print(thislist)
# >>>Sort the list descending :
# thislist=[9,8,56,34,2,5,77,40,30,12]
# thislist.sort(reverse=True)
# print(thislist)
# >>customize sort function <<<
# your own function by using the keyword argument.
# key=function.
# the function will return a number that will be used to sort the list(the lower number first)
# e.x
# sort the list based on how close the number is to 50:
# def myfunc(n):
#     return abs(n-50)
# thislist=[100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)
# >>case Insesitive Sort<<<<
# sort() method is case sensitive resulting in all capital letters beging sorted before lower case letter.
# E.x
# case sensitive sorting can give an unexcted result.
# thislist=["banana","Orange","Kiwi","cherry"]
# thislist.sort()
# print(thislist)
# >>>if you want a case-sensitive sort function ,use str.lower as a key function.
# E.x
# thislist=["apple","Banana","cherry","Blackcurrent","mango","Papaya"]
# thislist.sort(key=str.lower)
# print(thislist)
# >>reverse order.
# if you want to reverse the order of a list regardless of the alphabet?
# the reverse() method reverses the current sorting order of the element
# E.x
# Reverse the order of the list items.
# thislist=["apple","banana","cherry","blackcurrent","mango","papaya"]
# thislist.reverse()
# print(thislist)
#                                              *******