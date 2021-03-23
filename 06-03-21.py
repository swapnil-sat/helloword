#
# >print('hello world')
# ==================================================================================
# >ADD TWO NUMBERS
# num1=2
# num2=6.35
# sum=num1+num2
# print(num1,'+',num2,'=',sum)
# ==================================================================================
# >Program to add two numbers entered by the users
# num1=int(input('Enter first number:'))
# num2=int(input('Enter second number:'))
# sum=float(num1+num2)
# print(num1,'+',num2,'=',sum)
# print(type(sum))
# ==================================================================================
# >Find the squre root of a given number
# num=25
# num_sqrt=num**0.5
# print('the squre root of ',num , 'is',num_sqrt)
# ==================================================================================
# > use of '\n' (this is used for take a distance between one or more lines
# print('first line \n\n')
# print('second line')
# ==================================================================================
# >take a input from the users
# name=input('Enter name:')
# print('Hello',name)
# ==================================================================================
# >Input () Function returns string
# a=input('Enter something: ')
# print(a)
# ==================================================================================
# Converting string to int and float
# a= '55'
# integer_number=int(a)
# float_number=float(a)
# print('Integer _number :',integer_number )
# print('float _number :', float_number )
# ==================================================================================
# >int and float string
# a=80
# b=80.99
# str_a=str(a)
# str_b=str(b)
# print(str_a)
# print(type(a))
# print(str_b)
# print(type(b))
# ==================================================================================
# >Error during type conversion
# a='hello'
# integer_number=int(a)
# print(a)
# ==================================================================================
# >Error during type conversion (Part II)
# a='55.5'
# b=float(a)
# print(b)
# print(type(b))
# ==================================================================================
# >Flat can't convert in to integer value ****************
# a='55.5'
# b=int(a)
# print(b)
# print(type(b))
# ==================================================================================
# > Loss of information during conversion
# float_number=6.27
# integer_number=int(float_number)
# print("float number",float_number)
# print ("Integer number",integer_number )
# ==================================================================================
# **********************************************************************************
# PYTHON OPERATORS
# **********************************************************************************
# What is an operators ?
# An Operator is a special symbol that carries out arithmetic or logical computation
# a=5
# sum=a+10
# print(sum)
# here a and 10 is operands
# + is operators
# Arithmetic operators like mathematical operations +,-,*,/,// etc
# ==================================================================================
# >Operator
# appling various arithmetic operators
# x=1
# y=2
# z=3.0
# result=x+y+z
# print(result)
# ==================================================================================
# >Concatenate two string.
# first_name ='swapnil  '
# last_name='Satras'
# Full_name=(first_name + last_name)
# print('Full Name is :',Full_name )
# ==================================================================================
#  - Operator
# a=12
# b=9
# result=a-b
# print(result)
# a=12.0
# b=9
# result=a-b
# print(result)
# ==================================================================================
# * Operator
# a=5
# b=14
# result=a*b
# print (result)
# >Another Example
# result=1.4*5
# print(result)
# ==================================================================================
# >Multiply given string
# a='satras\n\n\n'
# repeat 'satras' string 3 times
# b=a*3
# print (b)
# >Error
a='satras\n\n\n'
# repeat 'satras' string 3 times
# b=a*'3'
# print (b)
# ==================================================================================
# / and // operator
# the / operator is used to divide left operand by the right one
# result=14/3
# print(result)
#  /  this are used for value or output given in float format
# result=14//3
# print(result)
#  //  this are used for value or output given in integer format
# ==================================================================================
# > % operator
# the modulus operator % gives the remainder of the division
# result=13%5
# print(result)
# result=8%2.5
# print(result)
# ==================================================================================
# > ** Operator
# the exponent operator **raises the left operand to the power of the right .for example 2**5 means 2 raised to the power of 5
# result=2**5
# print(result)
# base=2.5546
# power=6.5344
# result=base**power
# print(result)
# ==================================================================================
# > Assignment Operators
# this operators are used for assign values to the variables
# e.g
# a=5
# b='swapnil satras'
# ==================================================================================
# > = Operator
# x=100
# x=x+5
# print(x)
# ==================================================================================
# Example 2
# a,b,c= 5,5.2,'hello'
# print(a,b,c)
# x=y=z='swapnil satras'
# print(x,y,z)
# ==================================================================================
# >Assignment operator
# x=10
# x+=5     # x=x+5
# print(x)
# x=10
# x //=4      #x=x/4
# print(x)
# ==================================================================================
# >Operator precedence
# print(10-4*2)
#  operator precedence means sequence of arthmetic operation performance
# print((10-4)*2)
# **********************************************************************************
# Operator precedence list
# **********************************************************************************
# from higer level to lower level list
# ()
# **
# +*,-*
# *,/,//,%
# +,-
# **********************************************************************************
# a=3.44
# b=3
# result=a+b
# print(type(result))
# **********************************************************************************
# BOOLEN EXPRESSION
# what is loop?
# Loop is exacute statements repeatelly until a certain condition is satisfied
# E.g
# print(5>6)
# True and False are in this way case sensitive
# **********************************************************************************
# >COMPARISION OPERATORS
# this operator is used for the compare values. True or False according to the condition

# Operator                      Expression                      Result
# 1. >- Greater than            6>5                             True
# 2. <- less than               6<5                             False
# 3. ==- Equal to               6==5                            False
# 4. !=- Not equal to           6!=5                            True
# 5. >=- Greater than or equal to 6>=5                          True
# ====================================================================================
# >Examples
# x=10
# y=12
# print(x>y)
# print(x<y)
# print(x==y)
# print(x==10)
# print(x!=y)
# print(x!=10)
# print(x>=10)
# print(x>=20)
# print(x<=y)
# print(x<=10)
# ====================================================================================
# >LOGICAL OPERATORS
# and ,or,not
# Operator                      Meaning
# 1.and                           True if both operands are true
# 2.or                            True if either of the operands is true
# 3.not                           True if the operand is false
# ====================================================================================
# and Operator
# print(True and True)  #True
# print(False and True) #False
# print(False and False) #False

# a,b,c=1,2,3
# print(b>a and c>a)
# print(c>a and c<0)

# or Operator
# an expression containing or operator evaluates to True if either of the operands is true
# print(True or True)    #True
# print(False or True)   #True
# print(False or  False)  #False
# a=1
# b=2
# c=3
# print(b>a or c>a)
# print(c<0 or c>a)
# print(c==4 or b!=2)
# >not operator
#  An Expression containing not operators is True if the operands is False
# print(not True) #False
# print(not False ) #True
# x=5
# print(not (x!=5))
# print(not(x==5))
# ***********************************************************************************
# if .......else statement
# it is used for a decision making
# syntax of if......else statement
# if
#     boolen _expression :
#     statement(s)
# ====================================================================================
# Examples
# number=5
# if number>0:
#     print('number is positive')
# print('this is always executed')
#
# number = -1
# if number > 0:
#     print('number is positive.')
# print('this is always executed.')
# ====================================================================================
# if .......else statement
#     syntax
# if
#     boolen_expression :
#     statement(s)
#     else
#     statement(s)
# number=3
# if number>=0:
#     print('positive or zero')
#     print('the body of if is executed')
# else:
#     print('negative number.')
#     print('the body of else is executed')
# number=-5
# if number>=0:
#     print('positive or zero')
#     print('the body of if is executed')
# else:
#     print('negetive or zero')
#     print('the body of else executed')
# ====================================================================================
# > Python if_____elif______else
# ====================================================================================
# if you need to make a choice from more than 2 option ,you can use elif part in the if____else statement
# syntax
# if
#     boolen expression:
#     statement(s)
#     elif
#     boolen expression
#     statement(S)
# else:
#     statement(s)
# ====================================================================================
# example
# num=0.0
# if num>0:
#     print('positive number')
# elif num==0:
#     print('zero')
# else:
#     print('negetive number')
# ====================================================================================
# >Nested if .......else
# we can have an if....else statement inside another if ....else statement this is called nesting in computer programing
# ====================================================================================
# Example
# num=float(input('enter a number:'))
# if num>=0:
#     if num==0:
#         print('zero')
#     else:
#         print('positive number')
# else:
#         print('negative number')
# ====================================================================================
# >Example-simple calculator
# print('what operation do you want?')
# operator=input("Enter either +,-,* or divide")
# n1=float(input("Enter first number:"))
# n2=float(input('Enter second number:'))
# if operator=='+':
#     print(n1,operator,n2,"=",n1+n2)
# elif operator=='-':
#     print(n1,operator,n2,"=",n1-n2)
# elif operator=='*':
#     print(n1,operator,n2,"=",n1*n2)
# elif operator=='/':
#     print(n1,operator,n2,"=",n1/n2)
# else:
#     print('Invalid operator')
# ====================================================================================
# >while loop
# a loop is used to repeat a block of code as long as the  boolen expression is true in this lesson we will learn about while loop
# the syntax of while loop is :
#     while
#         boolen _expression :
#         statement(S)
# ====================================================================================
# Examples
# n=3
# i=1
# while i<=n:
#     print('loop is easy')
#     i=i+1
# ====================================================================================
#   Iteration                   Variable                    i<=n                    Body of loop
#     1st                         n=3 ,i=1                     true                   loop is easy printed i is incresed to 2
#     2nd                         n=3,i=2                       true                loop is easy printed i is increased  to 3
#      3rd                        n=3,i=3                       true                loop is easy printed i is increased to4
#       4th                       n=3,i=4                       false               loop is terminated
# ====================================================================================
# infinite loop
# n=3
# i=1
# while i<=n:
#     print( "loop is easy.")
#     i=i+1
# ====================================================================================
# >Infinite while loop
# n=3
# i=1
# while i<=n:
#     print("loop is easy.")
#     print("infinite loop is also easy")
#====================================================================================
# while True :
#     print("This statement will run endlessly.")
#     print("This statement will also run endlessly")
# ====================================================================================
# Sum of natural Numbers
# n=10
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print("the sum is",sum)
# ====================================================================================
# While Loop with else
# counter=0
# while counter <3:
#     print("Inside loop")
#     counter=counter+1
# else:
#     print("inside else")
# ====================================================================================
# Example:Multiplication table
# n=14
# i=1
# while i<=10:
#     print(n,'x',i,'=',n*i)
#     i=i+1
# ====================================================================================
#>FOR LOOP
# this is used for iterate over a sequence or other iterable objects.
# >Sequence
# three sequences
# String-
# a string is sequence of a characters
# text='python programming'
# Lists-
# A list is a sequence of items separated by commas and enclosed in squre brackets e.g
# My_list =[2,'test',5.6]
# Range()
# it is used to create a sequence of numbers .e.g
# numbers=range(1,6)
# >for loop
# syntax
# for val in sequence :
#     statement(s)
# e.g
# languages=['java','python','c++']
# for item in languages:
#     print(item)
# ====================================================================================
# >Sum from 1 to 100
# numbers=range(1,101)
# sum=0
# for i in numbers:
#     sum +=i
#     print('sum=',sum)
# ====================================================================================
# >Multiplication table
# n=14
# for i in range (1,11):
#     print(n,'X',i,'=',n*i)
# ====================================================================================
# for loop with else
#
# the else part is executed once all the items in the sequence exhaust
# my_list=[5,"Hello"]
# for item in my_list :
#     print(item)
# else:
#     print("inside else")
# ====================================================================================
# >Break and continue introdution
# break and continue statement can alter the flow of a normal loop
# sometime we may need to terminate the loop immediately without checking the test expression .for that ,break statement is used

# ====================================================================================

# ====================================================================================||
# ||         PYTHON BREAK STATEMENT                                                   ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# sometime we may need to terminate the loop immediately without checking test expression for  that break statement is used
# e.g
# numbers=[1,5,0,-4,10,9]
# for val in numbers:
#     if val < 0:
#         break
# print(val)
# ====================================================================================||
# sum=0
# while True:
#     n=input('Enter a number:')
#     n=float(n)
#     if n<0:
#         break
#         sum+=n
# print("sum=",sum)
# ====================================================================================||
# ||         PYTHON BREAK STATEMENT                                                   ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# > continue statement
# the continue statement is used to skip the rest of the code inside a loop for the current iteration only . loop does not terminate but continues on with the next iteration.
# ====================================================================================||
# ||           PASS STATEMENT                                                         ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# this is where pass statement is used .it is used to construct a body that does nothing
# E.g
# sequence ={'p','a','s','s'}
# for val in sequence:
#     pass
# print('Statement after loop')
# ====================================================================================||
# >More on pass
# sequence={'p','a','s','s'}
# for val in sequence
#     # Comment
# ====================================================================================||
# ||           Control Flow Examples                                                  ||
# ||                                                                                  ||
# ||                                                                                  ||
# ||==================================================================================||
# >Find the laegest Among Three numbers
# num1=-5
# num2=12
# num3=8
# if  (num1>=num2)and(num1>=num3):
#     largest=num1
# elif(num2>=num1) and(num2>=num3):
#     largest=num2
# else:
#     largest=num3
#     print('the largesr number is',largest)
# ====================================================================================||
# >Check leap year
# year = 2000
# if(year%4)==0:
#     if(year%100)==0:
#         if (year%400)==0:
#             print(year,'is  a leap year')
#         else:
#             print(year,'is a leaf year')
#     else:
#         print(year,'is not a leap year')
# ====================================================================================||
# >Generate Fibonacci sequence
n_terms=10
n1=0
n2=1
count=0
print('Fibonacci sequence up to ',n_terms,":" )
while count<n_terms:
    print(n1,end=)