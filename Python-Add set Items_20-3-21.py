# ====================================================================================||
# ||         Python-Add  Set Items                                                    ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>Add Items<<<<
# Once a set is created you cannt change its items but you can add new items.
# to add one item to a set use the add() method.
# E.x
# Add an item to a set using the add() method.
# thisset={"apple","banana","cherry"}
# thisset.add("orange")
# print(thisset)
# >>Add sets <<<<
# to add items from another set into the current set,use the update()method.
# E.x
# Add element from tropical and thisset into newset:
# thisset={"apple","banana","cherry"}
# tropical={"pineapple","mango","papaya"}
# thisset.update(tropical)
# print(thisset)
# >>add any Iterable<<<<
# the object in the update() method doesnot have be a set, it can be any iterable object (tuple,lists,dictionary)
# E.x
# Add element of a list to at set:
# thisset={"apple","banana","cherry"}
# mylist=["kiwi","orange"]
# thisset.update(mylist)
# print(type(thisset),thisset)
#                                           *****