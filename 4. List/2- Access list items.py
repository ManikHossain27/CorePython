#Print the second item of the list:
thislist = ['apple', 'banana', 'cherry']
print(thislist[1])

#Negative indexing
'''
    Negative indexing means start from the end
    -1 refers to the last item, -2 refers to the second last item etc.
'''
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])

#Range of Index
#Return the third, fouth and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Range of Negative indexing
#returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:
#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

