# ====================================================================================||
# ||         Python - Format- Strings                                                 ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>String Format<<<<<
# here we can combine strings and numbers by using the format() method!
# the format() methods takes the passed arguments,formats them ,and places them in the string where the placeholders{}are:
# E.g
# use the format() method to insert numbers into string.
# age=36
# txt="My name is John,and I am {}"
# print(txt.format(age))
# the format() method takes unlimited number of arguments and are placed into the respective placeholders.
# E.g
# quantity=3
# itemno=567
# price=49.95
# myorder="I want{} pieces of item{} for{} dollars."
# print(myorder.format(quantity,itemno,price))
# you can use index numbers{0} to be sure the arguments are placed in the correct placeholders:
# quantity=3
# itemno=567
# price=49.95
# myorder="I want to pay {2} dollers  for {0}pieces of item {1} ."
# print(myorder.format(quantity,itemno,price))
#                                                           ****
