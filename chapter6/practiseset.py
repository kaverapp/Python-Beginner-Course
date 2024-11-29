#write a program to find the greatest of four numbers entered by the user
'''
a=int(input("enter num1 :"))
b=int(input("enter num2 :"))
c=int(input("enter num3 :"))
d=int(input("enter num4 :"))


if(a>=b and a>=c and a>=d):
    print(a)
elif(b>=c and b>=d):
    print(b)
elif(c>=d):
    print(c)
else:
    print(d)

        #  (or)

print(max(a,b,c,d))   # Prints the largest number
'''

#write a program to find out wether a student has passed or failed if it requires  total of 405 and at least 33% in each subject to pass .Assume 3 subjets and take marks as input from the user
'''
_mark1_=int(input("enter mark1 :"))
_mark2_=int(input("enter mark2 :"))
_mark3_=int(input("enter mark3 :"))

total=_mark1_+_mark2_+_mark3_
percentage=(total/300)*100

if(_mark1_>=33 and _mark2_>=33 and _mark3_>=33 and percentage>=40):
    print("you are pass")
else:
    print("you are fail")
    '''

# a spam comment is defined as a text containing following keywords:
# "Make a lot of Money"," buy now","Subscribe this","click this".Write a program to detect these spams

'''
a=input("enter any text :").lower()
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

if (a in spam_keywords ):
    print("this is spam")
else:
    print("this is not spam")
    '''

# write a program to find wether a username entered has at least 10 characters or not

'''
_usrname_=input("enter username :")

if(len(_usrname_)<10):
    print(" username is less than 10 characters")
else:
    print("username is greater than 10 characters")
'''

# write a proram which finds out  wether a given name is present in a list or not

'''
_name_=input("enter your name :").lower()

_namelist_=["rohan","fathima","begum","latha","rahul","preeti"]
if(_name_ in _namelist_):
    print("ypur name is present in the list")
else:
    print("your name is not present in the list")
    '''

#write a program to calculate he grade of a student from his marks from the following scheme:

'''
_marks_=int(input("enter your marks :"))

if(_marks_>90):
    print("grade -ex")
elif(_marks_>80 and _marks_<90):
    print("grade A")
elif(_marks_>70 and _marks_<80):
    print("grade B")
elif(_marks_>60 and _marks_<70):
    print("grade C")
elif(_marks_>50 and _marks_<60):
    print("grade D")
else:
    print("grade Fail")
'''

#write a program to find out wether a given post is talking about "Harry" or not
'''
_post_="this is my happy good life after HARRY school and home"

if("harry" in _post_.lower()):
    print("post is talking about harry")
else:
    print("not harry not you")
    '''