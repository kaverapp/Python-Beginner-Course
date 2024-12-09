# write a program to add two numbers ?
'''
a=5
b=67
print(a+b)
'''
# write a program to find  remainder when a number is divided by z ?
'''
a=33
b=25
print(a%b)
'''

# check the type of variable assigned using input() function

'''
a=input("enter any Number:")
print(type(a))
'''
#use a comparision operator to find out wether a  given variable is greater than "b" or not
#take a=34 and b=80
'''
a=34 
b=80
print(a>b)
'''

#write a python program to find an average of two numbers entered by the user

'''
a=int(input("enter any Number1:"))
b=int(input("enter any Number2:"))
print((a+b)/2)
'''

#write a program to calculate the square of nmbers enterd by the user

'''
a=int(input("enter any Number1:"))
print(a*a)
   #(or)
print(a**2)
'''

# Write a program to reverse a string and convert it to uppercase.
'''
a=input("enter any string:")
print("Input:",a)
print("Output:",a[::-1].upper())
'''

#Create a list of numbers from 1 to 10. Double each number in the list and print the result.
'''
lst=[]
a=input("enter any number:")
nums=[int(x) for x in a.split()]
for i in nums:
    lst.append(i)
print("Input:",lst)
lst=[i*2 for i in lst]
print("Output:",lst)
'''

#Create a dictionary that stores student names as keys and their marks as values. Write a program to print the marks of a student given their name.


'''
std_marks={
    "rakesh":90,
    "suresh":80,
    "rahul":70,
    "savitha":42,
    "suvarna":60

}


for key , value in std_marks.items():
    print(key,value)
    '''

#Given a tuple of three elements (e.g., (1, 2, 3)), unpack the values into three separate variables and print them.
'''
tup=(1,2,3)
print(tup[0])
'''

#Write a program to find the union and intersection of two sets.


'''
set1={1, 2, 3}
set2= {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
'''

#Intermediate
#Convert a list of integers [1, 2, 3] into a single string "123".

'''
lst=[1, 2, 3]
for l in lst:
    con=str(l)
    print(con,end="")

'''
#Write a program to count the occurrence of each character in a string using a dictionary.

'''
inp="hello"

stri=[x for x in inp]
cnt=f"{[stri.count(x) for x in stri]}"
cpy=set(stri)
print(cpy,cnt)'''

'''
inp="hello"
cnts={char:inp.count(char) for char in set(inp)}
print(cnts)
   '''

