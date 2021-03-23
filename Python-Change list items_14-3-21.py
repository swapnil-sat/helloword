# ====================================================================================||
# ||         Python-Change List Items                                                 ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>Change item value
# to change the value of a specific item,refer to the index number.
# E.x
# change the second item.
# thislist=["apple","banana","cherry"]
# thislist[1]="blackcurrant"
# print(thislist)
# thislist=["apple","banana","cherry"]
# thislist[1]="mango"
# print(thislist)
# >>>Change a range of item values:
# change the value of items within a specific range ,define alist with the new values,and refer to the range of index numbers where you
# want to insert the new values:
# E.x
# change the values "banana" and "cherry"with the values "blackcurrant"and "waterlemon"
# thislist=["apple","banana","cherry","orange","kiwi","mango"]
# print(thislist)
# thislist[1:3]=["balckcurrant","waterlemon"]
# print(thislist)
# >>>if you insert more items than you replace the new items will be inserted where you specified and the remaining items will momve
# accordingly.
# E.x
# change the second value by replacing it with two new values:
# thislist=["apple","banana","cherry"]
# thislist[1:2]=["balackcurrant","mango"]
# print(thislist)
# Note -the length of the list will change when the number of items inserted does not match the number of items are replaced
# insert less items than you replace ,the new items will be inserted where you specified and the remaining items will move accordingly.
# E.x
# change the seconnd and third value by replacing it with one value.
# thislist=["apple","banana","cherry"]
# thislist[1:3]=["waterlemon"]
# print(thislist)
# >>>>Insert Items<<
# to insert a new list item,without replacing any of the existing values,we can use the insert()method
# the insert() method inseerts an item at the specified index:
# E.x
# insert "waterlemon"as the third item:
# thislist=["apple","banana","cherry"]
# thislist.insert(2,"waterlemon")
# print(thislist)
# Note=as a rtesult of the example above the list will now contain 4 items
#                                            ******