# ====================================================================================||
# ||         Python - String Mothods                                                  ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >it has a set of buit-in -methods that you can use on string.
# >All string methods return new value .they do not change the original string .
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#1.capitalize()                                         Converts the first character to upper case.
# ______________________________________________________________________________________________________________________
# txt="process finished with exit code"
# print(txt.capitalize())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#2.casefold()                                        Converts  string into lower case.
# ______________________________________________________________________________________________________________________
# txt="PROSSES FINISHED WITH EXIT CODE"
# print(txt.casefold())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#3.center()                                         Returns a centered string .
# ______________________________________________________________________________________________________________________
txt="abcd"
print(txt.center(3,"*"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#4. count()                                         Returns the number of times a specified value occurs in a string  .
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.count("f"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#5. encode()                                         Returns an encoded version of the string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.encode( ))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#6.endswith()                                         Returns  true if the string ends with the specified value
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.endswith("e"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#7.expandtabs()                                          sets the tab size of the string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.expandtabs())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#8.find()                                           Searches the string for a specified value and returns  the position of where it was found
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.find("P"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#9.format()                                          formats specified value in a string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.format())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#10.format_map()                                          formats specified value in a string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.format_map())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#11.index()                                           Searches the string for a specified value and returns the position of where it was found
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.index("e",5))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#12.isalnum()                                           Returns true if all characters in the string are alphanumaric
# ______________________________________________________________________________________________________________________
# txt= "1234fgdf"
# print(txt.isalnum( ))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#13.isalpha()                                           Returns true if all characters in the string are alphabet
# ______________________________________________________________________________________________________________________
# txt="Swapnil 7ras"
# print(txt.isalpha())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#14.isdecimal()                                           Returns true if all characters in the string are decimals  # ______________________________________________________________________________________________________________________
# txt="12345678"
# print(txt.isdecimal())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#15.isdigit()                                           Returns true if all characters in the string are  digit
# ______________________________________________________________________________________________________________________
# txt="1234567890"
# print(txt.isdigit())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#16.isidentifier ()                                           Returns true if the string is an identifier
# ______________________________________________________________________________________________________________________
# txt="India is my Country all indian are my brother and sister"
# print(txt.isidentifier())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#17.islower()                                           Returns true if all characters in the string are lower case
# ______________________________________________________________________________________________________________________
# txt="process is very difficult"
# print(txt.islower())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#17.isnumeric()                                           Returns true if all characters in the string are numeric
# ______________________________________________________________________________________________________________________
# txt="Swapnil 7ras "
# print(txt.isnumeric())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#17.isprintable()                                           Returns true if all characters in the string are printable
# ______________________________________________________________________________________________________________________
# txt="Swapnil Satras"
# print(txt.isprintable())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#18.isspace()                                           Returns true if all characters in the string are whitespaces
# ______________________________________________________________________________________________________________________
# txt="The numarical value sign of the charge"
# print(txt.isspace())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#19.istitle()                                           Returns true if the string follows the rules of a tital
# ______________________________________________________________________________________________________________________
# txt="India is My Country"
# print(txt.istitle())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#20.isupper ()                                           Returns true if all characters in the string are upper case
# ______________________________________________________________________________________________________________________
# txt="India is my country"
# print(txt.isupper())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#21.join()                                           join the element of an iterable tp the end of string
# ______________________________________________________________________________________________________________________
# txt="Indian people are helpful"
# print(txt.join("a"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#22.ljust()                                           Returns a left justified version of the string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.ljust())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#23.lower()                                            converts a string into lower case
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.lower())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#24.lstrip()                                           Returns a left trim version of the string
# ______________________________________________________________________________________________________________________
# txt="Process finished with exit code"
# print(txt.lstrip())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#25.maketrans()                                        Returns a translation table to be used in translation
# ______________________________________________________________________________________________________________________
# txt="Swapnil Satras"
# print(txt.maketrans())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#26.partition()                                        Returns a tuple where the string is parted into three parts.
# ______________________________________________________________________________________________________________________
#
#
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#27.replace()                                        Returns a string where a specified value is replaced with a specified value
# ______________________________________________________________________________________________________________________
# txt="Swapnil Satras"
# print(txt.replace("Swapnil","Vijay"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#28.rfind()                                        Searches the string for a specified value and returns the last position of where it was found
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rfind("d"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#29.rindex()                                        Searches the string for a specified value and returns the last position of where it was found
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rindex("d"))
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#30.rjust()                                         Returns a right justified version of the string
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rjust())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#31.rpartition()                                         Returns a tuple wherethe string is parted into three parts
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rpartition())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#32.rsplit()                                          Spits the string at the specified separator ,and returns a list
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rsplit())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#33.rstrip()                                           return a right trim version of string
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.rstrip())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#34.split()                                            Split the string at the specified separator,and returns a list
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.split())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#35.splitlines ()                                            Split the string at line breaks and returns a list
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.splitlines())
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#36.startswith()                                             Returns true if the string starts with the specified value
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.startswith("S"))
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#37.strip()                                             Returns a trimmmed version of the string
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.strip())
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#38.swapcase()                                              Swaps cases lower case becomes upper case and vice versa
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.swapcase())
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#39.tital()                                              Convert the first character of eachword to upper case
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.title())
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#40.translate()                                             Returns a translated string
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.translate())
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#41.upper()                                             Converts a string into upper case
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.upper())
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Method                                                                Description .
#42.zfill()                                              Fills the string with a specied number of 0 values at the  beginning
# ______________________________________________________________________________________________________________________
# txt="Searches the string for a specified value and returns the last position of where it was found"
# print(txt.zfill())
# ______________________________________________________________________________________________________________________
#                                                                           ****
