#Loops
  #loops are used to repaet instructions



 
#while condition:
    #block of code to be executed
    #condition is checked before each iteration



# now i want to print hello world 5 times what can i do i will use print 5 times


                                           # print("hello world \n"*5)
                                           # #or
                                           # print("hello world")
                                           # print("hello world")
                                           # print("hello world")
                                           # print("hello world")
                                           # print("hello world")
'''___________________________________________________________________________'''
#while loop


'''
i=0                              # here i is iterator
while i<=5:                      #iteratons
    print("hello world",i)
    i=i+1
    '''

#     output--->
#        hello world 0
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# hello world 5


'''
i=5                              # here i is iterator
while i>=0:                      #iteratons
    print("hello world",i)
    i=i-1
'''
#     output--->
#     hello world 5
# hello world 4
# hello world 3
# hello world 2
# hello world 1
# hello world 0


#lets practise
          # print numbers from 100 to 1
'''
i=100
while i>=0:
    print(i)
    i-=1
    '''
        #print the elements of following list using loop [1,4,9,16,25,36.49.64.81.100]

'''
i=1
while i<=10:
    print(i*i)
    i+=1
'''
        #search for this number x in this list tuple using loop [1,4,9,16,25,36.49.64.81.100]
'''
_target_=int(input("enter any number:"))
_list_=(1,4,9,16,25,36,49,64,81,100)
i=0
while(i<=len(_list_)-1):
    if(_target_==_list_[i]):
        print(_target_,"found at index",i)
    
         
    
    i+=1
'''





'''___________________________________________________________________________'''