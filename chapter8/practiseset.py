# .1  Basic Function Syntax 

# write a function to calculate and return the square of a number

'''
def sqr(num):
    return num*num
print(sqr(8))
'''

# .2 function with Multiple Parameters

#Create a function that takes two numbers as parameters and returns their sum
'''
def sum(num1,num2):
    return num1+num2
print(sum(10,37))
'''

# .3 Polymorphism in function

#  write a function multiply that multiplies two numbers. but can also accept and multiply strings
'''
def multiply(num1,num2):
    return num1*num2
print(multiply("hth",37))
'''

# .4 function returning multiple values

#create a function that returns both the area and circumference of a circle given its radius
'''
import math


def areacircum(radius):
    area=math.pi*(radius*radius)
    circumference=2*math.pi*radius
    return area,circumference

area,circum=areacircum(3)
print("area:",(area))
print("circumference:",(circum))
'''

# .5 function with default parameter value
#write a function that greets a user if no user is provided it should greet with a default name
'''
def greet(user="user"):
    print("hello",user)

greet("rohan")
greet()
'''

# .6 Lambda Function
#create a lambda function to compute the cube of a number

'''lamda function refers to function without name'''

'''
cube =lambda x:x**3
anothercube=cube(5)
print(anothercube)
'''

# .7 function with "arge"
#write a function that takes variable number of arguments and return their sum

'''
from ast import arg


def sum_all(*args):
    # print(*args)
    print(args)
    return sum(args)


print(sum_all(1,2,3))
print(sum_all(1,2,3,43,5,67,4))
print(sum_all(1,2,3,6,6,97,23,13))
print(sum_all(1,2,3,6,98,45,4))

'''


#wap using function to find greatest of three numbers
'''
def greatest(num1,num2,num3):
    if (num1>num2 and num1>num3):
        return num1
    elif(num2>num3):
        return num2
    else:
        return num3
print(greatest(10,20,30))
'''

#wap using function to convert celcius to gahreneit
'''
def convert(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit
print(convert(10))
'''

#how do you prevent a python print() function to print a new line at end

'''
def print_no_newline(arg):
    print(arg,end="")

print_no_newline("hello")
print_no_newline("world")
'''

#write a recursive function to calculate the sum of first n natural numbers

'''
def sum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+sum(n-1)
print(sum(5))
'''
#write a function to print first n lines of the following pattern
# ***
# **
# *
'''
def patrn(n):
    if n > 0:                 # Base case: stop when n reaches 0

        print("*"*n)
        patrn(n-1)

patrn(3)
'''

#wap function which converts inches to cms
'''
inch=1

def inchtocm(inch):
    cm=inch*2.54
    return cm
print(inchtocm(inch))
'''

#wap function to remove a given word from a list and strip it at the same time
'''
def strip_n(lst,rm_wrd):
    chck=rm_wrd.strip()
    s_rip=[item.strip() for item in lst if chck not in item.strip() ]
    print(s_rip)

lst=["harry1","larry2 "," harry3  "]

strip_n(lst,"harry")
'''