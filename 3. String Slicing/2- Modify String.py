a = ' Hello Manik '

#make upper case
print(a.upper())

#make lower case
print(a.lower())

#remove space before and/or after the actual text
print(a.strip())

#Replace character
print(a.replace('H', 'J'))

#splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))

#Format string: use variable in String
age = 36
txt = f"My name is John, I am {age}"
print(txt)