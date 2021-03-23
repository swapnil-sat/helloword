# ====================================================================================||
# ||         Python- join Sets                                                        ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>join Two Sets
# there are several ways to join two or more sets in pyhton.
# you can use the union() method that returns a new set containing all items from both sets or the update() method that insert all
# the items from one set into another:
# E.x
# the union()method returns a new set with all items from both sets:
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)
# E.x
# the update() method insert the items in set2 into set1:
# set1={"a","b","c"}
# set2={1,2,3}
# set1.update(set2)
# print(set1)
# Note=Both union() and update() will exclute any duplicate items.
# Keep ONLY the duplicates
# the intersecction_update()method will keep only the items that are present in both sets-
# E.x
# keep the items that exist in both set x and sety:
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# x.intersection_update(y) find a common element
# print(x)
# the intersection()method will return a new set that only contain the itmes that are present in both set
# E.x
# Return a set that contains the items that exist in both set x and sety:
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# z=x.intersection(y)
# print(z)
# Keep All ,But NOT the Duplicates
# the symmetric_difference _update() method will keep only the elemets that are NOT present in both .
# E.x
# Keep the items that are not present iin both sets:
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# x.symmetric_difference_update(y)
# print(x)
# the  symmetric_difference_update() method will return a new set that contains only the element that are NOT present in both
# E.x
# return a set that contains all items from both sets except items that are present in both :
# x={"apple","banana","cherry"}
# y={"google","microsoft","apple"}
# z=x.symmetric_difference(y)
# print(z)
#                                                           *****