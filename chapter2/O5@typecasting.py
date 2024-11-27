#type function and type casting

#check the type
'''
a="any name"
print(type(a))  #<class 'str'>

a=10
print(type(a))  #<class 'int'>

a=10.5
print(type(a))  #<class 'float'>

a=True
print(type(a))  #<class 'bool'>

a=None
print(type(a))  #<class 'NoneType'>

a=10
b=20
print(type(a+b))  #<class 'int'>    

a=10
b=20.5
print(type(a+b))  #<class 'float'>


a=10
b=True
print(type(a+b))  #<class 'int'>

a=10
b=None
print(type(a+b))  #<class 'NoneType'>
'''

#type casting
'''
print(type(int("10")))   #<class 'int'>
print(type(float("10"))) #<class 'float'>
print(type(str(10)))     #<class 'str'>
print(type(bool(10)))     #<class 'bool'>
print(type(bool(0)))     #<class 'bool'>
print(type(bool(None)))   #<class 'bool'>
print(type(bool(False)))  #<class 'bool'>
print(type(bool(True)))   #<class 'bool'>
print(type(bool(1)))     #<class 'bool'>
print(type(int(1.56)))     #<class 'int'>
'''