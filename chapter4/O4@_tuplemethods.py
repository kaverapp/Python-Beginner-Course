 #methods in tuple

 #@1 count
'''
_my_tuples=(1,3,5,3,6,7)
print(_my_tuples.count(3))    #output=>2   it gives output because tuple is immutable it dosent act like list
'''
#@2 index '''index(value, [start], [end])'''
'''
_mtup2_=(2,5,78,0,True,"hello")
print(_mtup2_.index(0,2,5))     #output=> 3
print(_mtup2_.index(0))         #output=> 3
'''
#@3 slicing and indexing
'''
m_tuples=(2,5,78,0,True,"hello")
print(m_tuples[0:3])            #output=>(2, 5, 78)
print(m_tuples[:3])             #output=>(2, 5, 78)
print(m_tuples[2:])             #output=>(78, 0, True, 'hello')
print(m_tuples[-1:])            #output=>('hello',)
'''

#@4 unpacking -assigning tuple elements to variables

'''
m_tuples=(2,4,7,True)
a,b,c,d=m_tuples
print(a,b,c,d)            #output=>2 4 7 True
'''

#@5 Converting a Tuple to a List
'''
m_tuple=(1,4,5)
m_list=list(m_tuple)
print(m_list)
'''
#@6 Converting a List to a Tuple

'''
m_list=[1,4,5]
m_tuple=tuple(m_list)
print(m_tuple)
'''

#@7 membership operators
'''
m_tuple=(1,4,5)
print(4 in m_tuple)       #output=>True
print(3 in m_tuple)       #output=>False
print(3 not in m_tuple)   #output=>True
'''

#@8 min and max

'''
m_tuple=(1,4,332,5,8)
print(min(m_tuple))       #output=>1
print(max(m_tuple))       #output=>332
'''