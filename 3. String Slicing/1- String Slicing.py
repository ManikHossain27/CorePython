#Slice from char 2 to 5 (before 5)
b = "Hello, World!"
print(b[2:5])

#Slice from start
b = "Hello, World!"
print(b[:5])

#Slice to the end
b = "Hello, World!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
