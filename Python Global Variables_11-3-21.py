# ====================================================================================||
# ||         Python Global Variables                                                  ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >variables that are created  outside of a function (as in all of the example above )are know global variables/.
# it is used by everyone both inside of function and outside.
# e.g
# create a variable outside of a function and use it inside the function .
x="Awesome"
def myfunc():
    print("python is",+x)
    myfunc()