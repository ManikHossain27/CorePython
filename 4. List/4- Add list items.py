#append(), insert(), extend(),

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To insert a list item at a specified index, use the insert() method.
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method.
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Add any iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ['apple', 'banana', 'orange']
thistupe = ('kiwi', 'cherry')
thislist.extend(thistupe)
print(thislist)