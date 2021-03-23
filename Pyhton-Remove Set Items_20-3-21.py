# ====================================================================================||
# ||         Python-Remove  Set Items                                                 ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>Remove Items<<<
# to remove an items in a set use remove() or the discard() method.
# E.x
# Remove "banana" by using the remove() method:
# thisset={"apple","banana","cherry"}
# thisset.remove("banana")
# print(thisset)
# Note-if the item to remove does not exist ,remove()will raise an error.
# E.x
# remove "banana"by using the discard() method
# thisset={"apple","banana","cherry"}
# thisset.discard("banana")
# print(thisset)
# Note :if the item to remove doesnot exist,discard() will NOT raise an error.
# the pop() method to remove an item ,but this method will remove the last item. remember that sets are unordered ,so you
# will not know what item that gets removed.
# the return value of the pop() method is remove item.
# E.x
# Remove the last item by using the pop() method:
# thisset={"apple","banana","cherry"}
# x=thisset.pop()
# print(x) banana is out from the given set
# print(thisset)
# Note-sets are unordered ,so when uusing the pop() method you do not know which item that gets removed.
# E.x
# the clear() method empties the set:
# thisset={"apple","banana","cherry"}
# thisset.clear()
# print(thisset)
# E.x
# the del keyword will delet the set completely.
# thisset={"apple","cherry","banana"}
# del thisset
# print((thisset))
#                                                   *******