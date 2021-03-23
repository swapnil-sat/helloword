# ====================================================================================||
# ||         Regular Expression                                                       ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# it is sequence of characters that forms a search pattern.it is used to check if a string contain the specified search pattern
# >RegEx Module
# python has a built in package called 're',which can be used to work with regular expressions.
# import the re module:
# import re
# when you have imported the re module you can start using regular expressions :
# >Example
# import re
# txt="The rain in Spain"
# x=re.search("^The.*Spain$",txt)
# if x:
#     print('YES! we have a match!')
# else:
#     print("no match")
#||==================================================================================||
# >RegEx Functions
# the re module offers a set of functions that allows us to search a string for a match.
# Function                                                          Descriotion
#1. findall                                   Returns a list containing all matches
#2.search                                      Returns a match object if there is a match anywhere in string
# 3.Split                                       Returns list where the string has been split at each match
# 4.sub                                         Replaces one or many matches with a string
# >METACHARACTERS.
# >Metacharacters are characters with a special meaning
# Character             Description                 Example
# 1.[]                  A set of characters         [a-m]
# e.g
# import re
# txt="The rain in spain" #Find all lower case characters alphabetically between 'a' and 'm'
# x=re.findall("[a-m]",txt)
# print(x)
# ______________________________________________________________________________________________________________________
# Character             Description                                                                         Example
# 2.\                   singnals a special sequence (can also be used to escape special characters)         "\d"
# e.g
# import re
# txt="That will be 59 dollars" #find all digit characters:
# x=re.findall("\d",txt)
# print(x)
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 3. '.'                    Any character(except newline character)                                         "he..o"
# e.g
# import re
# txt="hello world"
# # search for a sequaence that starts with "he",followed by two (any)characters and an "O":
# x=re.findall("he..o",txt)
# print(x)

# import re
# txt="Swapnil Satras"
# x=re.findall("Sw....l",txt)
# print(x)
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 4.^                       Start with                                                                          ^hello
# e.g
# import re
# txt="Hello World"
# # Check if the string starts with hello:
# x=re.findall("^Hello",txt)
# if x:
#     print("Yes,the string starts with hello.")
# else:
#     print("No match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 5.$                       End with                                                                            "World$'
# import re
# txt="hello world"
# # Check if the string ends with 'world':
# x=re.findall("world$",txt)
# if x:
#     print("Yes,the string ends with 'world'")
# else:
#     print("no match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 6.*                       Zero or more occurrences                                                            "aix*"
# e.g
# import re
# txt="The rain in spain falls mainly in the plain"
# check if the string contain 'ai'followed by 'O' or more 'x' characters.
# x=re.findall("aiX*",txt)
# if x:
#     print("Yes,there is at least one match")
# else:
#     print("no match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 7.+                       One or more occurances                                                              "aix+"
# e.g
# import re
# txt="The rain in spain falls mainly in the plain!"
# # Check if the string contains 'ai' followed by 1 or more 'x' characters:
# x=re.findall("aix+",txt)
# print(x)
# if x:
#     print("Yes,there is at least one match ! ")
# else:
#     print("No Match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 8.{}                      Exactly  the specified numbers of occurance                                         "al{2}"
# E.g
# import re
# txt ="The rain in Spain falls mainly in the plain!"
# Check if the string contains "a" followed by exactly two"1" characters:
# x=re.findall("al{2}",txt)
# print(x)
# if x:
#     print("yes ,there is at least one match!")
# else:
#     print("No Match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 9.|                         Either or                                                                      "falls|stays"
# e.g
# import re
# txt="The rain in Spain falls mainly in the plain!"
# # check if the string contains either "falls"or "stays":
# x=re.findall("falls|stays",txt)
# print(x)
# if x:
#     print("Yes,there is at least one match!")
# else:
#     print("No match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 10.()                     Capture and group
# ______________________________________________________________________________________________________________________
#  >Special sequences
# A special sequence is a\ followed by one of the character in the list below and has a special meaning.
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 1.\A                      Returns a match if the specified characters are at the beginning of the string      "\AThe"
# e.g
# import re
# txt="The rain in Spain"
# # Check if the string starts with "The":
# x=re.findall("\AThe",txt)
# print(x)
# if x:
#     print("Yes,there is a match!!!")
# else:
#     print("No match")
# ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 2.\b    Returns a match where the specified characters are at the begining or at the end of a word         r"\bain
#                                                                                                              r"ain\b
#E.g
# import re
# txt="The rain in Spain "
# # check if "ain" is present at the beginning of a WORD:
# x=re.findall("r\bain",txt)
# print(x)
# if x:
#     print("Yes,there is at least one match!")
# else:
#     print("No Match")
# >Another Example
# import re
# txt="The rain in the Spain "
# # Check if "ain" is present at the end of a WORD:
# x=re.findall(r"ain\b",txt)
# print(x)
# if x:
#     print("Yes,there is at least one match!")
# else:
#     print("No match")
 ______________________________________________________________________________________________________________________
# Character                 Description                                                                         Example
# 3.\B       Returns a match where the specified characters are present but not at beginning(or at the end )of a word