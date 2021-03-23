# ====================================================================================||
# ||         Python-  Unpack tuples                                                   ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>Unpacking a tuple.
# when you create a tuple we normally assign values to it this is called "packing"a tuple.
# E.x
# packing a tuples.
# fruits=("apple","banana","cherry")
# print(fruits)
# we are also allowed to extract the values back into variablles.this is called "unpacking"
# E.x
# unpacking a tuple.
# fruits=("apple","banana","cherry")
# (green,yellow,red)=fruits
# print(green)
# print(yellow)
# print(red
# the number of variables must match the number of value in the tuple if not you must use an asterix to collect the remianing
# values as a list.
# >>>>>Using Asterisk*
# if the number of variables is less than the number of values you can add an * to the variable name and the values will be
# assigned to the variable as a list.
# E.x
# assign the rest of the value as a list called "red":
# fruits=("apple","banana","cherry","strawberry","raspberry")
# (green,yellow,*red)=fruits
# print(green)
# print(yellow)
# print(red)
# if the asterix is added to another variable name than the last ,python will assign values to the number of values left matches the
# number of variable left.
# E.x
#Add a list of values the "tropic"variables.
# fruits=("apple","banana","papaya","pineapple","cherry")
# (green,*tropic,red)=fruits
# print(green)
# print(tropic)
# print(red)
#                                               ****