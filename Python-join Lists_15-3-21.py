# ====================================================================================||
# ||         Python- Join Lists                                                       ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>join Two Lists.
# there are several ways to join ,or concatenate ,two or more lists in python .
# one of the easiest ways are by using the + operator
# E.x
# joint two list:
# list1=["a","b","c"]
# list2=[1,2,3,4]
# list3=list1+list2
# print(list3)
# Another way to joint two lists are by appending all the items from list2 into list1,one by one:
# E.x
# append list2 into list1:
# list1=["a","b","c"]
# list2=[1,2,3,4]
# for x in list2:
#     list1.append(x)
#     print(list1)
# or you can use the extend() method which ppurpose is to add alement from one list to another list.
# E.x
# use the extend() method to add list2 at the end of list1:
# list1=["a","b","c"]
# list2=[1,2,3,4]
# list1.extend(list2)
# print(list1)
#                                                   ******