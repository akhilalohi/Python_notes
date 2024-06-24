#single line strings --> ',""
#Multiple line strings--> connector - /
# eg. "hello"/
#     "everyone" same line
# ''' hello 
#everyone''' different line as u want

#string indexing,slicing,negative slicing
#slicing synatax
#   str (start_index_pos : end_index_positions : Number_of_moves or jumps)
# strings r immutable
# string comparison
# >,<,== --> to check equality

'''string1= "Hello"
string2 = "hello"
print(string1<string2)'''

# ASCII codes
# A-Z = 65 to 96
# a-z = 97-122
# ord() --> gives ascii codes for characters
# chr()--> gives charavter value to ascii values
'''print(chr(65))
print(chr(97))'''

#string repeatation
# * to repeat string multiple times
# + to join many strings
'''string1= "hello"
string2="guys"
print(string1 + " " + string2)'''

#Find length or number of characters in a string
string1= "hello"
print("The number of characters in string are :", len(string1))

#test if a p-articular vcharacter of sub-string is present in a string or not
#membership test by in or not in ,find()
# find()--> if present return index of first char, if not returns -1
#index()--> if substring is absent then it will raise an error

#to covert upper--> upper()
#lower--> lower()
# replace syntax--> str1.replace('all','all the')

#to slice or split or cut the string
# split()--> str1.split() default separator is space ' '
# str1.split(',')
