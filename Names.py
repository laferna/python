# Assignment: Names
# Write the following function.

# Part I
# Given the following list:

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

>>> students = [
...      {'first_name':  'Michael', 'last_name' : 'Jordan'},
...      {'first_name' : 'John', 'last_name' : 'Rosales'},
...      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
...      {'first_name' : 'KB', 'last_name' : 'Tonel'}
... ]
>>> for x in students:
...     print x["first_name"],x["last_name"]
... 
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
>>> 

# Part II
# Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

 #TEST First:

 >>> users = {
...  'Students': [
...      {'first_name':  'Michael', 'last_name' : 'Jordan'},
...      {'first_name' : 'John', 'last_name' : 'Rosales'},
...      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
...      {'first_name' : 'KB', 'last_name' : 'Tonel'}
...   ],
...  'Instructors': [
...      {'first_name' : 'Michael', 'last_name' : 'Choi'},
...      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
...   ]
...  }
>>> 
>>> for user in users:
...     print user
... 
Students
Instructors
>>> 

# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

for user in users:
    print user;
    sum=1;
    for x in users[user]:
        print str(sum)+" - ",x["first_name"],x["last_name"],"-",(len(x["first_name"])+len(x["last_name"]));
        sum += 1;

# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. 
# Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.

#Running program into Python Shell:

>>> users = {
...  'Students': [
...      {'first_name':  'Michael', 'last_name' : 'Jordan'},
...      {'first_name' : 'John', 'last_name' : 'Rosales'},
...      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
...      {'first_name' : 'KB', 'last_name' : 'Tonel'}
...   ],
...  'Instructors': [
...      {'first_name' : 'Michael', 'last_name' : 'Choi'},
...      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
...   ]
...  }
>>> for user in users:
...     print user;
...     sum=1;
...     for x in users[user]:
...         print str(sum)+" - ",x["first_name"],x["last_name"],"-",(len(x["first_name"])+len(x["last_name"]));
...         sum += 1;
... 
Students
1 -  Michael Jordan - 13
2 -  John Rosales - 11
3 -  Mark Guillen - 11
4 -  KB Tonel - 7
Instructors
1 -  Michael Choi - 11
2 -  Martin Puryear - 13
>>> 