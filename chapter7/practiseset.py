#write a program to find the sum of first n num1bers (using while)


'''
n=int(input("enter any number:"))
sum=0
i=1
while i<=n:
    sum=sum*1+i
  
    i+=1
print(sum)
    '''

#wap to find the factorial of first n numbers (using for)
'''
n=5
flag=1
for i in range (1,n+1):
    flag=flag*i

print(flag) 
'''

#Write a program to calculate the sum of all even and odd numbers between 1 and n\

'''
n=int(input("enter any number:"))
even=0
odd=0

for i in range(1,n+1):
    if(i%2==0):
        even=even*1+i
        
        # print(i,"even")
    else:
        odd=odd*1+i
        # print(i,"odd")

print("this is odd Number :",odd)
print("this is even Number :",even)
'''

# *****************************************************************8
'''#Use a while loop to count the number of digits in an integer.

n=int(input("enter any number:"))
print(n)
i=0
while(i<=n):
    print(i)
    i+=1'''
#*****************************************************************

#wap to Use a while loop to reverse the digits of a given number.






#hitesh bhai

#counting positive Numbers
#given a list of numbers =[1,-2,3,-4,5,6,-7,-8,9,10]

'''
numbers =[1,-2,3,-4,5,6,-7,-8,9,10]
count=0

for i in range(0,len(numbers)):
    if(numbers[i]>0):
        count+=1
        # print(numbers[i],"is positive",i,count)
    else:
        pass
        
    
print(count,"positive numbers")

    '''

#MUltiplicaion table printer

'''
_table_=int(input("enter any number:"))

for i in range(1,11):
    print(f"{_table_}X{i}={_table_*i}")
    '''

#REverse a string

n="hello hi"

'''
for i in range (len(n)-1,-1,-1):
    print(n[i])

'''
'''
i=len(n)-1
while(i>=0):
    print(n[i])
    i-=1
'''

#sum of even numbers
'''
n=10
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum*1+i
        print(i,sum)
    else:
        print("this is odd number")
print(sum)
'''