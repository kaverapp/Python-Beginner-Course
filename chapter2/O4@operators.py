#OPERATORS

'''
5 + 3 here 5 and 3 are operands and + is an operator
'''
#Arithmetic operators
'''
print(5 + 3)  # Output: 8   
print(5 - 3)  # Output: 2
print(5 * 3)  # Output: 15
print(5 / 3)  # Output: 1.6666666666666667
print(5 % 3)  # Output: 2
print(5 ** 3)  # Output: 125
print(5 // 3)  # Output: 1
'''

#Comparison operators
'''
print(5 == 3)  # Output: False
print(5 != 3)  # Output: True
print(5 > 3)   # Output: True
print(5 < 3)   # Output: False
print(5 >= 3)  # Output: True
print(5 <= 3)  # Output: False'''


#Assignment operators
'''
x = 5
x += 3    # x = x + 3
print(x)  # Output: 8
x -= 3    # x = x - 3
print(x)  # Output: 5
x *= 3    # x = x * 3
print(x)  # Output: 15
x /= 3    # x = x / 3
print(x)  # Output: 5.0
x %= 3    # x = x % 3
print(x)  # Output: 2.0
x **= 3   # x = x ** 3
print(x)  # Output: 8.0
'''

#Logical operators
'''
print(True and True)  # Output: True
print(True and False) # Output: False
print(False or True)  # Output: True
print(True or False)  # Output: True
print(not True)       # Output: False
print(not False)      # Output: True
'''

#Membership operators
'''
print (2 in [1,4,2,7,8])  #True
print (2 in [1,4,7,8])    #False
print(2 not in [1,4,7,8])  #True
print(2 not in [1,4,2,7,8])  #False
print(2 in (1,4,7,8))      #False
print(2 in (1,4,2,7,8))    #True
print(2 not in (1,4,7,8))  #True
print(2 not in (1,4,2,7,8))  #False
print(2 in {'a':1,'b':2,'c':3})  #True
print(2 in {'a':1,'b':3,'c':4})  #False
print(2 not in {'a':1,'b':3,'c':4})  #True
'''

#Identity operators
'''
x = 5
y = 5
print(x is y)  # Output: True
print(x is not y)  # Output: False

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False  because x and y are different objects and are assigned to different memory locations, But  print(x == y)  # Output: True  because x and y are equal lists and have the same elements. 

'''

    
