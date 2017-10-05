#Fernandez_Python_Assignment: Fun with Functions
#Create a series of functions based on the below descriptions.

Odd/Even:
#Create a function called odd_even that counts from 1 to 2000. 
#As your loop executes, print the number of that iteration and specify whether it's an odd or even number.

#Your program output should look like below:

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

>>> def odd_even():
>>> for x in range(1, 2001):
...     if x % 2 == 0:
...             print x, "is an even number."
...     else:
...             print x, "is an odd number."
... 
1 is an odd number.
2 is an even number.
3 is an odd number.
4 is an even number.
...
2000 is an even number.

__________

Multiply:
#Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
#and returns a list where each value has been multiplied by 5.
#The function should multiply each value in the list by the second argument. For example, let's say:

#a = [2,4,10,16]

#Then:

#b = multiply(a, 5)
#print b

#Should print [10, 20, 50, 80 ].


>>> def multiply(arr, num):
...     for x in range(0, len(arr)):
...             arr[x] *= num
...     return arr
... 
>>> numbers_array = [3, 6, 8, 10, 67]
>>> 
>>> print multiply(numbers_array, 5)
[15, 30, 40, 50, 335]
>>> 


