#create a simple list
'''list1= [1,2,3,"abs", True,11.89,4+5j]
print(list1)
'''
#create blank list
'''list2=[]#empty list
print(list2)'''

#list here in python is also a class. A list object can be also instantiate by list class
# constructor by invoking list()

'''str1 = "hello all"'''
# to convert this string directly to list we can invoke list()
'''new_list = list(str1)
print(new_list)
'''
#propertirs of list
#1.ORDERED
#2.mutable
#3.allows repeated values i.e. duplication
#1.ordered
#each element of list has an index position attached
'''list1=[1,2,3,"hello", "bye",3+7j,11.6]
print(list1[-4])'''

#slice and negative list
#2.mutable
#to add new element at th end of the list append()
'''list1=[1,2,3,"hello", "bye",3+7j,11.6]
list1.append('new value')
print(list1)'''

#to add new element at a specific position in list insert()
# insert() syntax= list1.insert(index_no. ,object)
'''list1=[1,2,3,"hello", "bye",3+7j,11.6]
list1.insert(4,'new value')
print(list1)'''

#you can add new values from another list into original list extend()

'''list2=[6,7,8,9]

list1.extend(list2)
print(list1)'''
#concatenation
'''print(list1+list2)'''
#list repeatation
'''print(list1*3)'''

#make modifications in list
#we can change a particular list element
'''list1=[1,2,3,"hello", "bye",3+7j,11.6]
list1[2]=30
list1[2:4]=[30,"hello all",5+4j]
print(list1)'''

#remove elments from the list remove()
'''list1=[1,2,3,"hello", "bye",3+7j,11.6]
list1.remove("hello")
print(list1)'''
#also used to find whether a number exist or not

#count() to count the occurence of elements
'''list1=[1,2,3,9,8,7,6,5]
print(list1.count("hello"))'''

#sort a list
'''list1.sort()#ascending order
print(list1)'''
#sorting in descending order
'''list1.sort(reverse=True)
print(list1)'''

#create a copy of list copy()
'''new_list=list1.copy()
print(new_list)'''

#tuple is a sequence similar to list but with some difference
#1. list is muatble tuple is not
#2. tuple starts with()
#3. there are only 2 methods in tuples while in list there are fairly good method

#create a tuple
'''tup1=(1,2,3,"hello",    True, False, 4+5j)
print(tup1)'''
#we have tuple constructor
'''new_tuple=tuple(('hello','bye',1,2,3,"go"))
print(new_tuple)
list1=list(tup1)
print(list1)
string1=str(tup1)
print(string1)'''
#empty or blank tuple
'''tup1= ()
print(tup1,type(tup1))'''
#create a typle w only single variab;e---> normal value unless comma
'''tup1=("hello")
print(tup1, type(tup1))'''#string
#if tup1 =25 the typw would be integer
#singleton tuples -->special feature of tuples unlike list
'''tup1=(34,)
print(tup1,type(tup1))'''

#default structure--> tuple
'''values= 1,2,3,4,4
print(values, type(values))'''

#properties for tuples
#1. ordered
#2. immutable
#3. allows duplicate values

#1.ordered
'''tup1=(1,2,3,"hello",    True, False, 4+5j)
print(tup1[1], tup1[1:6:2])'''
#2.immutable
'''tup1[4]=4'''#error

#to find count of elements len()
'''tup1=(1,2,3,"hello",    True, False, 4+5j)
print(len(tup1))'''

#check for membership in tuple
'''print("hello" in tup1)'''#true

#no direct removal methods allowed
#however u can remove entire tuple in one go
#del property
'''del tup1
print(tup1)'''

#two methods in tuple:
#1. count(): count the number of times or frequency of elemennt
#2. index(): search first occurence and find index of an element otherwisethrow exception
# index() only gives the first ones index if any element is repeated

#set
#1. set begin with {} braces
# 2. set does not allow duplicates
# 3. constructor call set()
#4. unordered

set1={1,2,3,"hello","bye",2,3,4,True, False}# would only take false not true # sometimes true==1 hence wont print 1
set2={5,3,4,6,7,8,9}
print(set1)
#empty set using set()
'''set2= {}#dictionary
set2= set()#set
print(type(set2))#typle by default
list2= []
print(type(list2))'''

#set is mutable
# to add new elements in set use add()
'''set1.add(55) # added anywhere , only one argument allowed
print(set1)'''

#update()--> to add elements from another list of tuples in a set
#similar to extend() in list
'''list1=[2,3,4,5,6]
set1.update(list1)
print(set1)'''

#we can rmeove original value from set remove()# discard()
set2= set1.remove(False)
print(set2)
set2= set1.discard(False)
#in remove() it will throw error if not found, discard wont throw error
#set operations : Union, INTERSEction, difference










