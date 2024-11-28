# union, intersection,difference
_s1_={1,2,3,4,5}
_s2_={6,7,8,9,5}

# union:
print(_s1_.union(_s2_))    #output=>{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
print(_s1_.intersection(_s2_))    #output=>{5}


#difference
print(_s1_.difference(_s2_))    #output=>{1, 2, 3, 4}
print(_s2_.difference(_s1_))    #output=>{8, 9, 6, 7}

#symmetric difference
print(_s1_.symmetric_difference(_s2_))    #output=>{1, 2, 3, 4, 6, 7, 8, 9}

#subset
print(_s1_.issubset(_s2_))    #output=>False

#superset
print(_s1_.issuperset(_s2_))    #output=>False
