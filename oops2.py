##class student:
##    name='rajesh'
##    email='r@gmail.com'
##    contact='9463493'
##    age=31
##    address='thane'
##
##    def show(s):
##        print(s)
##        print('python developer')
##
##s=student()
##print(s.name)
##print(s.email)
##
##s.show()
##print(s)
##
##
##print(student.name)
##
##print(student.contact)
##
##
###student.show('hello')


##class student:
##    name='rajesh'
##    email='r@gmail.com'
##    contact='9463493'
##    age=31
##    address='thane'
##
##    def show(self):   # self is a default paramter that represent the instance of class
##        print(self)
##        print('python developer')
##
##s=student()
##print(s.name)
##print(s.email)
##
##s.show()
##print(s)
##
##
##print(student.name)
##
##print(student.contact)
##
##
##student.show('hello')


##
##class student:
##    name='rajesh'
##    email='r@gmail.com'
##    contact='9463493'
##    age=31
##    address='thane'
##
##    def show(self):   # self is a default paramter that represent the instance of class
##        print(self)
##        print('python developer')
##        print(s.contact)
##        print(self.contact)
##        print(student.contact)
##
##    def display(self):
##        print('java developer')
##
##s=student()
##
##s.show()
##s.display()



##class student:
##    
##    age=31
##    address='thane'
##
##    def show(self):   # self is a default paramter that represent the instance of class
##        name='rajesh'
##        email='r@gmail.com'
##        print(name,email)
##        
##        
##    def display(self):
##        print(name,email)  #error
##        
##        
##s=student()
##
##s.show()
##s.display()



##class student:
##    
##    age=31
##    address='thane'
##
##    def show(self,contact,gender):   # self is a default paramter that represent the instance of class
##        name='rajesh'
##        email='r@gmail.com'
##        print(name,email,contact,gender)
##        
##        
##    def display(self):
##        #print(name,email)  #error
##        print(name,email,contact,gender)
##        
##        
##s=student()
##
##s.show('27549284271','male')
###s.display()
##print(name,email,contact,gender)
##



##class student:
##    
##    age=31
##    address='thane'
##
##    def show(self):   # self is a default paramter that represent the instance of class
##        print('python developer')
##        
##        
##    def display(self):
##        print('java developer')
##        s.show()
##        self.show()
##        abc.show()  # error
##       
##        
##        
##s=student()
##s.show()
##s.display()
##
###s.display()


##
##class A:
##    name='rajesh'
##    age=31
##
##    def show(s):
##        s.address='thane'
##        s.email='r@gmail.com'
##
##        #print(address,email,s.name)
##
##    def display(self):
##        gender='male'
##        print(self.address)
##        print(a.email)
##
##
##a=A()
##a.show()
##a.display()
##



##class A:
##    def show(self,name,age,salary):
##        self.name=name
##        self.age=age
##        self.salary=salary
##
##    def display(self):
##        print('My name is',self.name)
##        print('my age is',self.age)
##        print('salary is',self.salary)
##
##a=A()
##a.show('Rajesh',31,70000)
##a.display()
##
##


##class A:
##    def show(self):
##        self.name=input('Enter your name: ')
##        self.age=int(input('Enter your age: '))
##        self.salary=int(input('Enter salary: '))
##
##    def display(self):
##        print('My name is',self.name)
##        print('my age is',self.age)
##        print('salary is',self.salary)
##
##a=A()
##a.show()
##a.display()
##
##b=A()
##b.show()
##b.display()


##
##class A:
##    def show(self,name,address):
##        print('python developer')
##    def display(self):
##        self.show('janvi','pune')
##        a.show('kedar','itvedant')
##        print('java developer')
##        
##a=A()
##a.show('rajesh','thane')
##a.display()
##
##




##class A:
##    def show(self,name,address):
##        print('name is',name)
##        print('address is',address)
##        print('python developer')
##    def display(self):
##        self.show('janvi','pune')
##        a.show('kedar','itvedant')
##        print('java developer')
##        
##a=A()
##a.show('rajesh','thane')
##a.display()
##
##

##class A:
##    a=10
##    b=20
##
##    def demo(s):
##        s.a=s.a+1
##        A.b=A.b+1
##        print(s.a,A.b)
##        
##x=A()
##x.demo()
##
##y=A()
##y.demo()
##
##z=A()
##z.demo()

#constructor: _init_ method runs automatically when object is created
# which is used for initialize the instance object

##class A:
##    def _init_(s):
##        s.name=input('Enter the name: ')
##        s.address=input('Enter address: ')
##        s.age=int(input('Enter age: '))
##
##    def display(s):
##        print('name is',s.name)
##        print('address is:',s.address)
##        print('age is:',s.age)
##
##x=A()
##
##x.display()
##        
##y=A()
##y.display()
##


##class A:
##    def _init_(self,name,address,age):
##        self.name=name
##        self.address=address
##        self.age=age
##
##
##    def display(self):
##        print(self.name)
##
##    def _str_(self):
##        return self.name+' '+self.address+' '+str(self.age)
##
##
##
##x=A('rajesh','thane',31)
##x.display()
##
##print(x)
##print(x)
##print(x)
##

# destructor:

# destructor is a member method of class
# it delete the memory of object
# it can be call with object
# name is _del_


# Garbage collector:

# A program to delete references

# it runs automatically

# it does memory management


##class A:
##    def show(s):
##        print('python developer')
##
##    def display(s):
##        print('java developer')
##
##    def _del_(s):
##        print('object deleted')
##
##    
##a=A()
##a.show()
##
##a.display()
##
##del a


# inheritance
# one class can  derive the properties of another class this process is known as inheritance
##class A:
##
##    a=10
##
##    def show(s):
##        print('python developer')
##
##class B(A):
##
##    b=20
##
##    def display(s):
##        print(s.b+B.b+x.b+s.a+A.a+x.a+B.a)
##        print('java developer')
##
##
##
##x=B()
##x.display()
##
##x.show()


# Types of inheritance
# 1) single level inheritance


# Polymorphism

# Polymorphism means many form
# An entity can work in multiple role.this capability is called as polymorphism
# 1) function overriding  2) function overloading


# in function overriding we can declare a function in base class and derived class with same name and
# same parameter
# it occures when one class is inherit from another class(inheritance)


##class A:
##    def display(self):
##        print('python developer')
##
##class B(A):
##    def display(self):
##        print('java developer')
##
##
##ob=B()
##ob.display()


# more than one function with same name defined in same class and call with defferent parameter
# this process is known as method overloading
# but python does not support method overloading

##class A:
##    def show(self):
##        print('Hiii')
##    def show(self,x):
##        print('bye')
##    def show(self,x,y):
##        print('hello')
##
##a=A()
###a.show()  #hello
###a.show(10)  #hi
##a.show(10,30) #bye

##
##class A:
##    def show(self,x,y):
##        print(x+y)
##
##a=A()
##a.show(10,30)
##
##
##
##class A:
##    def show(self,x=90,y=100):
##        print(x+y)
##
##a=A()
##a.show(10,30)


##
##class A:
##    def show(self,x=None,y=None):
##        print(x+y)
##
##a=A()
##a.show(10,30)
##
##
##
##class A:
##    def show(self,a=None,b=None,c=None):
##        if(a!=None and b!=None and c!=None):
##            print(a+b+c)
##        elif(a!=None and b!=None):
##            print(a+b)
##        else:
##            print(a)
##        
##            
##x=A()
##x.show(10)
##x.show(2,3)
##x.show(10,20,30)
##
##
##

##class A:
##    def show(self,a,b,c):
##        print(a+b+c)
##    def show(self,a,b):
##        print(a+b)
##    def show(self,a):
##        print(a)
##
##
##x=A()
##x.show(10,20,30)
##        

# Exceptional handeling An exception is an event, which occurs during
# the execution of a program, that interrupt the normal flow of the
# program's instructions.

# the try block which is used to test a block of code for errors.

# the except block used to handle the errors.


##print('python developer')
##a=int(input('Enter the first number: '))
##b=int(input('Enter the second number: '))
##try:
##    print(a/b)
##except:
##    print('exception handeled')
##print('java developer')
##



##print('Hiiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except:
##    print('list index out of range')
##print('Hello')
##



##print('Hiiii')
##a=[11,22,33,44,55]
##try:
##    print(a[len(a)])
##except Exception as e:
##    print(e)
##print('Hello')
##



##print('python developer')
##a=int(input('Enter the first number: '))
##b=int(input('Enter the second number: '))
##try:
##    print(a/b)
##except Exception as e:
##    print(e)
##print('java developer')
##
##


##print('python developer')
##
##
##try:
##    a=int(input('Enter the first number: '))
##    b=int(input('Enter the second number: '))
##    print(a/b)
##except Exception as e:
##    print('Value Error:',e)
##print('java developer')
##


##try:
##    print('Thane')
##    print(2/0)
##    print(int('demo'))
##    print('Dadar')
##
##except ZeroDivisionError as e:
##    print(e)
##    
##except Exception as e:
##    print('exception handeled',e)



##try:
##    print('Thane')
##    print(2/0)
##    print(int('demo'))
##    print('Dadar')
##    
##except Exception as e:
##    print('exception handeled',e)
##
##except ZeroDivisionError as e:
##    print(e)
##    


##try:
##    print('Thane')
##    #print(2/0)
##    print(int('demo'))
##    print('Dadar')
##   
##except Exception as e:
##    print('exception handeled',e)
##
##except ZeroDivisionError as e:
##    print(e)
##
##except ValueError as v:
##    print('value error',v)
##    



##try:
##    print('Thane')
##    #print(2/0)
##    print(int('demo'))
##    print('Dadar')
##   
##
##
##except ZeroDivisionError as e:
##    print(e)
##
##except ValueError as v:
##    print('value error',v)
##    
##
##except Exception as e:
##    print('exception handeled',e)
##
##except:
##    print('exception handeled')
##
##
##
##try:
##    print('Thane')
##    #print(2/0)
##    print(int('demo'))
##    print('Dadar')
##   
##except:
##    print('exception handeled')    # error // default axcept must be last
##







    


##except ZeroDivisionError as e:
##    print(e)
##
##except ValueError as v:
##    print('value error',v)
##    
##
##except Exception as e:
##    print('exception handeled',e)
##



##try:
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('Mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##
##except:
##    print('outer exception handeled')
##




##k=[]
##try:
##    print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('Mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##
##except:
##    print('outer exception handeled')
##
##

##k=[]
##try:
##    #print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('Mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##
##except:
##    print('outer exception handeled')
##
##
##else:
##    print('it will execute only when exception is not occured')
##



##
##k=[]
##try:
##    print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('Mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##
##except:
##    print('outer exception handeled')
##
##
##else:
##    print('it will execute only when exception is not occured')
##
##finally:
##    print('it always be executed')
##


##print('thane')
##raise NameError()
##print('Mumbai')




##print('thane')
##try:
##    raise NameError()
##except:
##    print('exception handeled')
##print('Mumbai')
##



##print('thane')
##try:
##    raise InvalidAgeError()
##except:
##    print('exception handeled')
##print('Mumbai')
##


##class InvalidAgeError(Exception):
##    pass
##
##print('thane')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print('exception handeled')
##print('Mumbai')
##



##
##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error detected'
##
##print('thane')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##print('Mumbai')
##
##




##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error detected'
##
##print('thane')
##try:
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##print('Mumbai')
##

##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid age detecte                                                                                                                                                                                                                                                                      '
##
##age=int(input('Enter Your name: '))
##if(age>=18):
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##    except Exception as e:
##        print(e)
##


##x=1
##while(x<11):
##    if(x==5):
##        continue
##    print(x)
##    x=x+1




##class A:
##    def _init_(self,name,age):
##        print('python developer')
##    def show(self):
##        print('Hii')
##
##class B(A):
##    def _init_(self,name,age):
##        super()._init_('raj',32)
##        print('java developer')
##
##    def display(self):
##        print('Hello')
##
##
##b=B('rajesh',31)
