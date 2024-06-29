#Global veriable x, Local variable overwrite global variable in a function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print()

#Override global variable in a function by using global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print('Python is', x)

myfunc()

print("Python is " + x)

