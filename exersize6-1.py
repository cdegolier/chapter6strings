#Exercise 1: Write a while loop that starts at the last character
#in the string and works its way backwards to the first character 
#in the string, printing each letter on a separate line, except backwards.

print ("This will reverse a string!")
userinput = input("Enter your string: ")
newstring = ""
for i in range(len(userinput)):
  index = (-i) - 1
  newstring = newstring + userinput[index]

print (newstring)
