#10.4.2017_Python_OOP_Lecture.

class Student(object):
    def _init_(self, name, email):
        self.name = name    
        self.email = email  
        self.numberOfBelts = 0
    def addBelt(self):
        self.numberOfBelts += 1
        return self
    def say(self, thing):
        print self.name, "says", thing
        return self

    amina = Student("Amina", "amina@google.com")
    # amina.numberOfBelts = 3
    print amina.name, amina.email, amina.numberOfBelts 

    #methods:  
    amina.addBelt().addBelt()
    print amina.nmae, amina.email, amina.numberOfBelts
    amina.say("get back to work")

    #CHAINING: calling another method
    amina.addBelth().addBelt().say("I have more belts")

    #Do not return self. instead, print self.

    #INHERITANCE: 

    class Person(object):
        def _init_(self, name, email):
            self.name = name    
            self.email = email  
    class Student(Person):
        def _init_(self, name, email):
            super(Student, self)._init_(name, email) 
            self.numberOfBelts = 0
            return self
        def addBelt(self): 
            self.numberOfBelts += 1
            return self
        def show(self)
            print self.name, "has", self.numberOfBelts, "belt(s)"
            return self
        def say(self, thing):
            super(Student, self).say(thing)
            print "something else"

    # bob = Person("Bob", "bob@gmail.com")
    #bob.say("hello")

    #jenny = Student("Jenny", "jenny@gmail.com")
    #jenny.say("goodbye")""

    # class MyNumber(int):
    #     def sayHello(self):
    #         print self, "says hello"

    #Modules and Packages
    #in ipython shell, type: "from datetime import datetime"
        datetime.now()
        datetime.now().strftime("%m/%d/%Y")

        from random import random, randrange
        print random()
        print range(1,11)

#Multi-Arguments
    #when you don't know the number of arguments, * is used to change the # of arguments.
>>> def test(*args):
...    for arg in args:
...        print arg
... 
>>> 
>>> test(1,2,3,4)
1
2
3
4
>>> def test(*args):
...     print type(args)
... 
>>> test(1,2,3,4)
<type 'tuple'>
>>> test([1,2,3,4])
<type 'tuple'>
>>> 

#you can add multi-words. Dictionary.

    

