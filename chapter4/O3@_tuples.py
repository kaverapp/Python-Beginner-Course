
'''a=(2,6,"hello",False,6.7)
print(type(a))             #output=> <class 'tuple'>
'''
#changes
'''
_a=(1)
_b=(1,)
print(type(_a))            #output=> <class 'int'>
print(type(_b))            #output=> <class 'tuple'>
'''
#tuples are immutable 
'''
_a=(2,"tuple",False,6.7)
_a[0]="hello"
print(_a)                  #TypeError: 'tuple' object does not support item assignment
'''