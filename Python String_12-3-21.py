# ====================================================================================||
# ||         Python String                                                            ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >>>>>String<<<<<<<
# strings in python are surrounded by either single quotation marks or double quotation marks.
# 'hello' is same as "hello"
# you can display a string literal with the print() function.
# E.g
# print('hello')
# print("hello")
# _____________________________________________________________________________________________________________________
# >>>Assign String to a variable<<<<
# the variable name followed by an equal sign and the string
# E.g
# a="Hello"
# print(a)
# >>>Multiline String<<<<
# assign a multiline string to a variable by using three quotes.
# E.g
# Three double quotes.
# a="""this is python language,python is fanstastic ,pyhton is awesome and better than other computer languages  """
# print(a)
# Three Single quotes.
# a='''this is python language,python is fanstastic ,pyhton is awesome and better than other computer languages '''
# print(a)
# _____________________________________________________________________________________________________________________
# >>>>Strings are Arrays<<<<<
# strings in python are are arrays of bytes representing unicode characters.
# python doesnot have a character data type ,a single character is simply a string with a length of 1
# squre brackets can be used to access element of the string
# E.g
# Get the character at position 1 (remember that the first character has position 0):
# a="hello"
# print(a[1])
# _____________________________________________________________________________________________________________________
# >>>> Looping through a string<<<<<<<
# Since strings are arrays ,we can loop through the characters in a string ,with a for loop
# E.g
# Loop through the letters in the word "Banana"
# for x in "Banana":
#     print(x)
# ______________________________________________________________________________________________________________________
# the len() function returns the length of a string:
# a="hello world"
# print(len(a))
# ______________________________________________________________________________________________________________________
# Check string
# to check if a certain pharase or character  is present in a string we can use the keyword in .
# E.g
# Check if "Python"is present in the following text.
# txt="python is awesome and funstatic"
# print("python"in txt)
# use it in an if statement
# E.g
# Print only if "free" is present .
# txt="The best things in life are free!!"
# if "free" in txt:
#     print("Yes,'free' is present")
# else:
#     print("Given Word is absent")
# ______________________________________________________________________________________________________________________
# >>>>Check if not <<<<<<<
# To check if a certain phrase or character is NOT present in a string ,we can use the keyword not in.
# E.g
# Check if "expensive" is NOT present in the following text.
# txt="The best things in life are free!"
# print("expensive" not in txt)
# ______________________________________________________________________________________________________________________
# >>>>Use it in an if  statement<<<<<<<
# e.g
# print only if "expensive" is not present
# txt="The best things in life are free"
# if "expensive" not in txt:
#     print("yes,'expensive'is NOT present")
#                                                           ***