#Fernandez_Python_Assignment: Finding_Characters

#Write a program that takes a list of strings and a string containing a single character, 
#and prints a new list of all the strings containing that character.

#Here's an example:
# input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# output
# new_list = ['hello','world']
# Hint: how many loops will you need to complete this task?


word_list = []
letters = set('')

for word in word_list:
    if letters & set(word):
        print(word)

#Checked on Python Shell:

>>> word_list = ['hello','world','my','name','is','Anna']
>>> letters = set('e')
>>> 
>>> for word in word_list:
...     if letters & set(word):
...             print(word)
... 
hello
name
>>> 
