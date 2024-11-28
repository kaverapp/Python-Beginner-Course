#write a program to store seven students in a list entered by the user
'''
fruit1 = input("Enter the name of fruit 1: ")
fruit2 = input("Enter the name of fruit 2: ")
fruit3 = input("Enter the name of fruit 3: ")
fruit4 = input("Enter the name of fruit 4: ")
fruit5 = input("Enter the name of fruit 5: ")
fruit6 = input("Enter the name of fruit 6: ")
fruit7 = input("Enter the name of fruit 7: ")

fruitStorage=[fruit1,fruit2,fruit3,fruit4,fruit5,fruit6,fruit7]
print(fruitStorage)
'''

#write a program to accept marks of 6 students and display them in a sorted manner
'''
marks=[]
student1 = (input("Enter the name of student 1: "))
student2 = (input("Enter the name of student 2: "))
student3 = (input("Enter the name of student 3: "))
student4 = (input("Enter the name of student 4: "))
student5 = (input("Enter the name of student 5: "))
student6 = (input("Enter the name of student 6: "))
student7 = (input("Enter the name of student 7: "))

marks=[student1,student2,student3,student4,student5,student6,student7]
print(marks)
marks.sort()
print(marks)
'''


#chec`k that tuple  cannot be changed in python`
'''
_chec_=(1,2,3,4,5)
_chec_[0]="hello"
print(_chec_)            #output=>ypeError: 'tuple' object does not support item assignment
'''

#write a program to sum a list with 4 numbers
'''
_list_=[1,2,3,4]
print(sum(_list_))   #output=>10
'''

#write a program to count the number of zeroes in the following tuple

'''
a=(7,0,8,0,0,9)
print(a.count(0))   #output=>3
'''