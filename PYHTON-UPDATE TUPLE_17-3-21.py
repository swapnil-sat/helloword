# ====================================================================================||
# ||         Python- Update tuples                                                    ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# tuples are unchangable meaning that you cannt change,add or remove items once the tuple created.
# but there are some workrounds.
# >>>>Change a tuplevalue
# once a tuple is created,you cant change its value tuples are unchangable or immutable as it also is called but there is a
#workround ,you can converted tuple into list,change the list and converted the list back into a tuple.
# E.x
# convert the tuple into a list to be able to change it:
# x=("apple","banana","cherry")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(type(x),x)
# Add Items <<
# once a tuple created ,you cannot add items to it.
# E.x
# you cannt add items to a tuple.
# thistuple=("apple","banana","cherry")
# thistuple.append("orange") this will raise an error
# print(thistuple)
# >>>just like the workaround for changing a tuple you can convert it into a list ,add your item(s),and convert it back into a tuple.
# E.x
# convert the tuple into a list add "orange"and convert it back in to a tuple.
# thistuple=("apple","banana","cherry")
# y=list(thistuple)
# y.append("orange")
# thistuple=tuple(y)
# print(thistuple)
# Remove items
# Note-you cannot remove items in a tuple.
# E.x
# thistuple=("apple","banana","cherry")
# y=list(thistuple)
# y.remove("apple")
# thistuple=tuple(y)
# print(thistuple)
# or you can delete the tuple completely.
# E.x
# the del keyword can delet the tuple completely.
# thistuple=("apple","banana","cherry")
# del.thistuple this will raise an error because the tuple no longer exist.
# print(thistuple)
