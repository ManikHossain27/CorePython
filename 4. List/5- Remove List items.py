# remove(), pop(), del(), clear()

#Remove Specified Item
#Remove 'banana'
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
#Remove the second Item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
#remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del keyword also remove the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() method emptist the list. The list remain, but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


