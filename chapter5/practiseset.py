#write a program to create a dictionary of hindi words with values as their english translawtion Provide user with an option to look it up

'''
_wordDict_={
    "ma":"mother",
    "papa":"father",
    "didi":"sister",
    "baiya":"brother",
    "mama":"uncle"
}
_opt_=input("enter a word for getting the meaning :").lower()
print(_wordDict_.get(_opt_))
'''

#write a program to input eight numbers from the user and display all the unique numbers (once)

'''
_ip1_=int(input("enter any number:"))
_ip2_=int(input("enter any number:"))
_ip3_=int(input("enter any number:"))
_ip4_=int(input("enter any number:"))
_ip5_=int(input("enter any number:"))
_ip6_=int(input("enter any number:"))
_ip7_=int(input("enter any number:"))
_ip8_=int(input("enter any number:"))

_set1_={_ip1_,_ip2_,_ip3_,_ip4_,_ip5_,_ip6_,_ip7_,_ip8_}
print(_set1_)
'''

#can we have a set with 18(int) and "18" (str) as a value in it ?
'''
_ch_={18,"18"}
_ch2_={18,18.0}
print(_ch_)        #yes
print(_ch2_)       #No      because Here, 18 (integer) and 18.0 (floating-point) are different types, but Python treats them as equal for set operations.hash(18) == hash(18.0) evaluates to True.18 == 18.0 also evaluates to True.

print(hash(18.0))       # Hash of integer 18
'''

#what will be the length of following set s:
'''
s=set()
s.add(20)
s.add(20.0)
print(len(s))      #output=>1
'''

#s={} what is the type of "s" ?
'''
s={}
print(type(s))   #output=><class 'dict'>
'''

#create an empty dictionary .Allow 4 friends to enter their favorite language as value and use key as their names.Assume that names are unique

'''
_dict_={
    "Rahul":input("enter any language:"),
    "Rohan":input("enter any language:"),
    "RaMU":input("enter any language:"),
    "RaGHU":input("enter any language:"),
}

print(_dict_)
'''

#if the names of two friends are same what will happen to program in problem 6

'''
_dict_={
    "Rahul":input("enter any language:"),
    "Rohan":input("enter any language:"),
    "RaMU":input("enter any language:"),
    "RaMU":input("enter any language:"),
}

print(_dict_)                 #output=>{'Rahul': 'python', 'Rohan': 'python', 'RaMU': 'python'} only the last item will be displayed
'''

#if languages of two friends are same what will happen to program in problem 6

_dict_={
    "Rahul":input("enter any language:"),
    "Rohan":input("enter any language:"),
    "RaMU":input("enter any language:"),
}

print(_dict_)                 #output=>{'Rahul': 'python', 'Rohan': 'python', 'RaMU': 'python'} 
