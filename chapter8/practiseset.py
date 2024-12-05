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