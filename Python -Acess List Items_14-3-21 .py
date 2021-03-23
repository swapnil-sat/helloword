# ====================================================================================||
# ||         Python-Access List Items                                                 ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>Access Items
# list items are indexed and you can access them by referring to the index number:
# E.x
# thislist=['apple','banana','cherry','pineapple']
# print(thislist[1])
# >>>>Note=the first item has index 0
# >>Negative indexing<
# it is starts from the end -1 refers to the last item,-2 refers to the second last item etc.
# E.x
# print the last item of the list.
# thislist=['apple','banana','cherry']
# print(thislist[-1])
# >>>>Range of indexes<<<<<
# Specify a range of indexes by specifying where to start andd where to end the range.
# when a specifying a range ,the return value will be a new list with the specified items.
# E.x
# Return the third ,fourth and fifth item.
# thislist=["apple","banana","Cherry","orange","kiwi","melon","mango"]
# print(thislist[2:5])
# note the search will start at index 2 (included)and end at index59not included)
# remember that the first item has index0
# E.x
# this example returns the item from the beginning to ,but NOT incuding ,kiwi:
# thislist=["apple","banana","cherry","kiwi","melon","mango"]
# print(thislist[:4])
# by leaving out the end value the range will go on to the end of the list
# E.x
# this eaxmple returns the item from"cherry" to the end :
# thislist=["apple","banana","cherry","orange","melon","mango"]
# print(thislist[2:])
# >>>>Range of negative indexes.
# negative indexes if you want to start theh search from the end of the list:
# E.x
# this eaxmple returns the items from "orange"(-4) to,but NOT including "mango"(-1):
# thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(thislist[-4:-1])
# check if items Exist.
# to determine if a specified item is present in a list use the in keyword:
# E.x
# Check if "apple"is present in the list.
thislist=["apple","banana","cherry"]
# if "apple"  in thislist:
#     print("Yes,'apple' is in the fruits list")
#                                           ******

