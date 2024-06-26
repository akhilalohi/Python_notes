#set
#unordered,no duplications, allows for advanced mathematical set operations
'''set1={1,2,3,4,5,6,7}'''
'''print(set1)'''

#we can add new values to set using add()
'''set1.add(99)#added anyuwhere
print(set1)
'''
#update() to update a set with a list,tuple or another set
'''list1=[7,8,9,10]
tup1=(11,22,33,44,55)
set2={666,888,999}
set1.update(list1)
print(set1)
set1.update(tup1)
print(set1)
set1.update(set2)
print(set1)
'''
#delete values from a set we can use remove() and discard()
#remove() throws an exception 'Key error' if the value is not found in set
#discard method simply does nothing if the value for deletion is not found


#Builtin methods of set
#all()--> checks for the True set of boolean values
#all() works for most of the iterators be it dictionaries, set, tuples, lists
'''set1={True,True,True,1,1,0,0,5,7,-11}'''#0 is the only specific off bit hence false, all other integers-->on bit
'''result= all(set1)
print(result)'''

#any() -->it returns True if atleast 1 value in an iterBLE is True
'''result= any(set1)
print(result)'''

#len()-->to check for lengty of a set
#true and 1 are considered same ,also, false and 0 are considered same
'''print(len(set1))'''

#max() and min()
'''res= max(set1)
print(res)#7
res= min(set1)
print(res)'''#-11

#sum()--> applicable to all iteratables
'''res= sum(set1)
print(res)'''

#Mathematical set operations
# Union, Intersection, symmetric difference, subtraction
#union -->combines unique elements from
#union() and |
'''set1={1,2,3,4,5}
set2={6,7,8,9,4,5}'''
'''print(set1.union(set2))
print (set1|set2)'''

#intersection: takes common elements from both sets
#intersection () and & operator
'''print(set1.intersection(set2))
print (set1&set2)'''

#difference() A-B : The elements of A subtraction the common elements with B
#The result must contain those elements A which are not present in B
#difference () and -minus operator
'''print(set1.difference(set2))
print (set1 - set2)'''

#in-place update operations
#intersection_update(), union_update(), difference_update()
'''set1.intersection_update(set2)
print(set1)'''
'''set1.update(set2)
print(set1)'''

#symmetric difference method()
#this method returns all the values present in given set datastructures except the common values between them
'''print(set1.symmetric_difference(set2))
'''
# symmetric_difference_update()
'''set1.symmetric_difference_update(set2)
print(set1)
print(set2)'''

#issuperset(), issubset(), isdisjoint()
'''set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9,10}'''
#check for subset and superset
'''print("If set1 is a subset of set2: ", set1.issubset(set2))
print("If set1 is a superset of set2: ",set1.issuperset(set2) )
print("If set2 is a subset of set1: ",  set2.issubset(set1))
print("If set2 is a superset of set1: ", set2.issuperset(set1))
print("If set1 and set2 are disjoint or not : ", set1.isdisjoint(set2))
'''

#pop() method : randomly deletes a value from set ; it updates the set and remove random element one by one
'''print("The removed value is: ",set1.pop())'''

#dictionary 
#key:value pair
#{} are brackets of dictionarry
#both set and dictionary are collection types so, they are unordered
#empty dictionary {} empty set ()

dict1={"Ename":"Ajay", "Age":20, "Salary":10000, "HouseNo":20}
'''print(dict1)'''
#access element in a dict
#w the help of keys
'''print(dict1['Salary'])'''
#dict r mutable
'''dict1['Degree']='BCA,MCA'
print(dict1)'''

#UPDATE existing value
'''dict1['Age']=22
print(dict1)'''

#remove value
#del prop
'''del dict1['Salary']
print(dict1)

res= dict1.pop('Age')
print(dict1)'''
#len(dict1)
'''print(dict1.keys())
print(dict1.values())
print(dict1.items())'''
#get() to get a value corresponding to a key
'''print(dict1.get('Age'))'''







