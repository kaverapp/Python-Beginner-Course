
#list methods
 #01 sort
'''
print(avengers.sort())     #TypeError: '<' not supported between instances of 'int' and 'str'

print(nums.sort())         #output=>None  beause, If you try to assign its result to a variable or print it directly, you'll see None.
nums.sort()
print(nums)                #[2, 5, 6.0, 8, 45, 45.0, 63]


#If you want to preserve the original list and get a new sorted list, use the sorted() function:
# sort(): Modifies the list in place and returns None.
# sorted(): Returns a new sorted list and leaves the original list unchanged.

copied_nums=sorted(nums)    #original nums list remains unchanged
print(copied_nums)          #[2, 5, 6.0, 8, 45, 45.0, 63]
print(nums)                 #[2, 5, 8, 6.0, 63,45,45.0]
'''

#02 reverse
'''
_copied_avengers = avengers[::-1]
# or
_copied_avengers=list(reversed(avengers))
print(_copied_avengers)

'''

#03 append
'''
avengers.append("black panther")
print(avengers)                     #output=>['thor', 'spiderman', 'ironman', 'hulk', 'captain america', 45, 89.07, True, 'black panther']
'''

#04 insert
'''
avengers.insert(0,"black widow")   #insert(index,value)
print(avengers)
'''