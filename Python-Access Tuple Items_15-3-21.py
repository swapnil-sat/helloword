# ====================================================================================||
# ||         Python-Access Tuple Items                                                ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >Access Tuple Items.
# access tuple by referring to the index number ,inside squre brackets.
# E.x
# print the second item in the tuple:
# thistuple=("apple","banana","Cherry")
# print(thistuple[1])
# > Note -the first item has index 0.
# >negative indexing.
# >it means start from the end
# -1 refers to the last item -2 refers to the second last item etc.
# E.x
# >print the last items of the tuple:
# thistuple=("apple","banana","cherry")
# print(thistuple[-1])
# >>>Range of indexes<<<<<
# indexes by specifying where to start and where to end the range .
# when specifying a range the return value will be a new tuple with the specified items.
# E.x
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(thistuple[2:5])
# Note -the search will start at index 2 (included) and end at index5(not included)
# first item has index0
# E.x
# this example returns the itemm from the beginning to,but NOT included ,"kiwi".
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(thistuple[:4])
# Example
# By leaving ou value the range will go on to the end of the list:
# E.x
# this example returns the items from "cherry"and to the end:
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(thistuple[2:])
#Range of negative indexes.
# it is used for you want to start the search from the end of the tuple:
# E.x
# this example returns the item from index -4(included) to index-1(excluded)
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(thistuple[-4:-1])
# check if item exists.
# to determine if a specified item is present in a tuple use in keyword.
# E.x
# check if 'apple' is present in the tuple.
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# if "apple" in thistuple:
#     print("yes,'apple' is in the thistuple")