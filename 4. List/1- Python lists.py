"""
    1. List is a collection which is ordered and changeable. Allows duplicate members.
    2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""


thislist = ["apple", "banana", "cherry"]
print(thislist)

#lists are ordered, changeable, allow duplicated items in lists

#duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print( len(thislist) )

#list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

#list type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#List Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)