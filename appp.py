###Using the "input" method in Python, ask a user to input a sentence. 
#Then develop a function that accepts a the user input and will tell you how many words are in that string. 
#First write out your plan in Pseudo-code using comments. 
#Then craft the function.
'''
x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
'''

x = input("Enter some words: ")
y = x.split( )

print (len(y))