# ====================================================================================||
# ||         Python-Add List Items                                                    ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>append items<<<<<
# to add an item to the end of the list use the append() method.
# E.x
# using the append() method to append an item:
# thislist=["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)
# >>>insert items<<<
# to insert a list item at a specified index ,use the insert() method.
# the insert() method insertes an item at the specified index:
# E.x
# insert an items as the second position:
# thislist=["apple","banana","cherry"]
# thislist.insert(1,"waterlemon")
# print(thislist)
# >>>Note-As a result of the examples above the list will now contain 4 items
# >>>>Extend list<<<<<<
# to append element from another list to the current list ,use the extend() method,
# E.x
# add the element of tropical to thislist.
# thislist=["apple","banana","cherry"]
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)
# the element will be added to the end of the list.
#>>>>>>add any iterable<<<<<<<
# the extend() method does not have to aapend lists,you can add any iterable object (tuple,sets ,dictionaries etc)
# E.x
# Add element of a tuple to a list .
# thislist=["apple","banana","cherry"]
# thistuple=("kiwi","orange")
# thislist.extend(thistuple)
# print(thislist)
#                                                       *******