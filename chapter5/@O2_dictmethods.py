from re import M


marks={
    "harry":100,
    "rohan":50,
    "karan":80,
    "list":[1,2,3,4,5],
    1:"one"
}


#keys and values

'''
print(marks.keys())         #output=>dict_keys(['harry', 'rohan', 'karan'])
print(marks.values())       #output=>dict_values([100, 50, 80])
'''

#items


'''
print(marks.items())      #dict_items([('harry', 100), ('rohan', 50), ('karan', 80), ('list', [1, 2, 3, 4, 5]), (1, 'one')])
'''


#clear

'''
marks.clear()
print(marks)               #output=>{}
'''

#copy

'''
copy_dict=marks.copy()
print(copy_dict)           #output=>{'harry': 100, 'rohan': 50, 'karan': 80, 'list': [1, 2, 3, 4, 5], 1: 'one'}
'''

#fromkeys  ->Creates a new dictionary with the given keys and sets the same default value for all keys.

'''
new_dict=dict.fromkeys(marks,0)
print(new_dict)             #output=>{'harry': 0, 'rohan': 0, 'karan': 0, 'list': 0, 1: 0}
           

# if no value is provided then default value is none
new_dict=dict.fromkeys(marks)
print(new_dict)  
'''

#get --> Returns the value of the specified key. If the key is not found, it returns the default value.

'''
print(marks.get("rohan"))       #output=>50
print(marks.get("rohan",100))   #output=>50   not 100 because it is default value given if no value is present
'''

#update
'''
marks.update({"rohan":1000,"rohan1":2000})
print(marks)
'''

#difference
 #get vs []

'''
print(marks["rohan"])         #output=>50
print(marks.get("rohan"))     #output=>50
 
print(marks["rohan2"])        #output=>KeyError: 'rohan2'
print(marks.get("rohan2"))    #output=>none
'''

#pop --to delete specific item from dictionary

'''
marks.pop("rohan")
print(marks)
'''