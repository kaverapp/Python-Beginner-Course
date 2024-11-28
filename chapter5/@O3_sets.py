#set ->set is a collection of non repetitive elements
#no repition allowed

_setele_={1,2,3,5,"harry"}

'''
print(type(_setele_))   #<class 'set'>
'''

'''
print(_setele_[0])     #TypeError: 'set' object is not subscriptable, The error occurs because sets in Python are unordered collections of unique elements, and they do not support indexing or slicing 
'''

'''
_setele_[0]="jaja"
print(_setele_)         #output=>TypeError: 'set' object does not support item assignment
'''

'''
_newset_={1,2,3,4,5,5,2,1,5,7,3,2,1}
print(_newset_)         #output=>{1, 2, 3, 4, 5, 7}   because  sets in Python are unordered collections of unique elements
'''

'''_emptyBrace_={}
print(type(_emptyBrace_))   #<class 'dict'>
'''


'''
newbrace=set()              #dont use set{} to create an empty set use set()
print(type(newbrace))       #<class 'set'>
'''


