#strings types

#sequence of characters enclosed in qoutes-single,double,triple code
# a='single qouted string'
# b="double qouted string"
# c='''triple qouted string'''
# d="""quadruple qouted string"""
# print(a,b,c,d)

#string slicing
'''
a="KAVERAPPA"         # K=0,A=1,V=2,E=3,R=4,A=5,P=6,P=7,A=8
b=a[0:3]              #here [0:3]==>'[start_index , end index]', the variable "a" contains a Name in which K is in 0th index

print(b)              #output: KAV
 
#negative slicing

a="KAVERAPPA"  
b=a[-1:0]        
print(b)
       

a="python"
b=a[0:4:2]             #substring = s[start : end : step]
print(b)               #output=> pt

a="hello world!"
a1=a[:]                #retrieve the entire string, use slicing without specifying any parameters.
print(a1)              #hello world!
print(a1[::])          #hello world!

b1="hello world run !"
b2=b1[::3]             #skip up  Every second character


c="hello world"
print(c[::-1])         #reverse a string  output=> `dlrow olleh`

'''

#strings are immutable you cannot change 

'''
_dummy="hello"
_dummy[0]="H"
print(_dummy)           #TypeError: 'str' object does not support item assignment
'''