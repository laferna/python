
#findAndReplace

>>> string="It's Thanksgiving day. It's my birthday, too!"
>>> print string
It's Thanksgiving day. It's my birthday, too!       //Print the position of the first instance of the word "day".
>>> print string.find("day")
18
>>> string=string.replace("day","month")            //Create new string where the word "day" is replaced with the word "month".
>>> print string
It's Thanksgiving month. It's my birthmonth, too!
>>> 


#MinAndMax

>>> x = [2,54,-2,7,12,98]
>>> print x
[2, 54, -2, 7, 12, 98]                              //Print the min value in list.
>>> print min(x)
-2
>>> print max(x)                                    //Print max value in the list.
98
>>> 


#FirstAndLast

>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> x[0]                                            //Print the first and last values in a list. Code should work for any list.
'hello'                                             
>>> x[len(x)-1]
'world'
>>> print [x[0],x[len(x)-1]]                        //Create new list containing only the first and last values in the original list. 
['hello', 'world']              
>>> 

#NewList
>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> print x
[19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]           //Sort list.
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]           //Then, split list in half.  
>>> first_list = x[:len(x)/2]
>>> second_list = x[len(x)/2:] 
>>> print "first list", first_list
first list [-3, -2, 2, 6, 7]
>>> print "second_list", second_list
second_list [10, 12, 19, 32, 54, 98]
>>> second_list.insert(0,first_list)                //Push the list created from the first half to position 0 of the list created from the second half.
>>> print second_list
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
>>> 


