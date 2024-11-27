
'''
a=input("Enter any Number:")
print(type(a))     #<class 'str'>    because, input field takes string 
 '''
#  what can i do now ,as i need to get number or integer as output so i need to convert string to integer
#  so i will use int() function to convert string to integer

'''
a=int(input("enter any Number:"))
print(type(a))                   #<class 'int'>
'''
#lets try to add userinput  without type casting

'''
a=input("enter any Number1:")   #4
b=input("enter any Number2:")   #5

print(a+b)                  #output will be "45
"'''

#lets try to add userinput  after type casting

'''
a=int(input("enter any Number1:"))   #4
b=int(input("enter any Number2:") )  #5

print(a+b)                  #output will be "9"
'''