##class student:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(s):
##        print('python developer')
##
##    def display():
##        print('java developer')
##
##s=student()
##print(s.name)
##print(s.age)
##print(s.address)
##
##s.show()

##
##class student:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self):   #self is default parameter that represent the instance of class
##        print('python developer')
##
##    def display(self):
##        print('java developer')
##
##s=student()
####print(s.name)
####print(s.age)
####print(s.address)
####
###s.show()
####s.display()
##
####print(student.name)
####print(student.age)
##
##student.show('hii')
##
##student.display('bye')
##



##class student:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self,name):   #self is default parameter that represent the instance of class
##        print(s)
##        print(self)
##        print(name)
##        print('python developer')
##
##    def display(self):
##        print('java developer')
##
##s=student()
####print(s.name)
####print(s.age)
####print(s.address)
####
##s.show('janvi')
##print(s)
##s.display()

##print(student.name)
##print(student.age)

##student.show('hii')
##
##student.display('bye')
##
##



##class A:
##    def demo(self):
##        print('Hii')
##
##    def display(self):
##        print('bye')
##        self.demo()
##
##a=A()
##
###a.demo()
##
##a.display()
##        


##class A:
##    def demo(self):
##        print('Hii')
##
##    def display(self):
##        print('bye')
##        a.demo()
##
##a=A()
##
###a.demo()
##
##a.display()
##        
##

##class A:
##    def demo(self):
##        print('Hii')
##
##    def display(self):
##        print('bye')
##        abc.demo()
##
##a=A()
##
###a.demo()
##
##a.display()
##        


### local variable: A variable which is present inside the method class is called as local variable and scope of local variable is
### inside the method only.
##class A:
##    def getdata(self,contact,gender):
##        name='rajesh'
##        address='thane'
##        print(name,address,contact,gender)
##
##    def show(self):
##        age=31
##        email='r@gmail.com'
##        print(name,address)
##
##
##a=A()
##a.getdata('345328459328','male')
###a.show()
##
##
##class A:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self):
##        self.contact='96392864'
##        self.email='e@gmail.com'
##
##        print(self.name,self.age,abc.address)
##
##
##abc=A()
##abc.show()
##


##
##class A:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self):
##        self.contact='96392864'
##        self.email='e@gmail.com'
##
##    def display(self):
##        self.dep_name='Extc'
##        print(self.contact)
##
##
##
##
##a=A()
##a.show()
##a.display()
##
##



##class A:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self):
##        print(self)
##        print(a)
##        self.contact='96392864'
##        self.email='e@gmail.com'
##
##    def display(k):
##        k.dep_name='Extc'
##        a.gender='male'
##        
##        print(k.contact,a.gender)
##
##    def demo(r):
##        print(r.contact)
##
##    def demo1(hii):
##        print(hii.contact,a.name,hii.email,a.gender)
##        
##
##
##
##
##a=A()
##a.show()
####a.display()
####
####a.demo()
####a.demo1()
##print(a)
##
##



##class A:
##    name='rajesh'
##    age=31
##    address='Thane'
##
##    def show(self):
##        print(self)
##        print(a)
##        self.contact='96392864'
##        self.email='e@gmail.com'
##
##    def display(k):
##        k.dep_name='Extc'
##        a.gender='male'
##        
##        print(k.contact,a.gender)
##
##    def demo(r):
##        print(r.contact)
##
##    def demo1(hii):
##        print(hii.contact,a.name,hii.email,a.gender)
##        
##
##a=A()
##a.show()
##a.display()
##a.demo()
##a.demo1()
##
##print(a.age,a.contact)
##
##print(a.age,self.contact)  # self.contact==> error



##class A:
##    name='rajesh'
##    age=31
##    email='r@gmail.com'
##    address='mulund'
##
##    def show(self):
##        contact='4432'
##        self.address='Thane'
##        print(A.name)
##
##    def display(self):
##        self.gender='male'
##        print(A.address)
##        print(a.address)
##
##a=A()
##a.show()
##print(A.name)
##a.display()
        
##class A:
##    name='rajesh'
##    age=31
##    email='r@gmail.com'
##    address='mulund'
##
##    def show(self):
##        pass
##        contact='4432'
##        A.address='Thane'  
##        print(A.name)
##        print(A.address)
##
##    def display(self):
##        self.gender='male'
##        print(A.address)
##        print(a.address)
##
##a=A()
####a.show()
####print(A.name)
####a.display()
##
##A.show('hi')

        
##class A:
##    a=10
##    b=20  #22
##    def show(s):
##        s.a=s.a+1
##        A.b=A.b+1
##        print(s.a,A.b)  #11,21
##
##x=A()
##x.show()
##
##y=A()
##y.show()
##
##z=A()
##z.show()
##
##


# constructor: _init_ method runs automatically when object is created
# which is used to initialize the instance object

##class A:
##    
##        
##    def _init_(s):
##        s.id=10
##        s.name='Rajesh'
##        s.salary=70000
##
##    
##        
##    def display(s):
##        print('id is',s.id)
##        print('name is',s.name)
##        print('salary is',s.salary)
##
##a=A()
##a.display()
###a.display()
###a.show()
###a.display()
##
##

##class A:
##    
##        
##    def _init_(s):
##        s.id=int(input('Enter id: '))
##        s.name=input('Enter Your name: ')
##        s.salary=int(input('Enter salary: '))
##
##    
##        
##    def display(s):
##        print(f'id is {s.id} name is {s.name} and salary is {s.salary}')
####        print('name is',s.name)
####        print('salary is',s.salary)
##
##a=A()
##a.display()
###a.display()
###a.show()
###a.display()
##
##x=A()
##x.display()

##class A:
##    def _init_(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name,s.age,s.salary)
##
##
##a=A('rajesh',31,70000)
##a.display()
##



##class A:
##    def _init_(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name,s.age,s.salary)
##
##
##
##    def _str_(s):
##        return s.name+' '+str(s.age)+' '+str(s.salary)
##
##
##a=A('rajesh',31,70000)
##a.display()
##
##print(a)


##class A:
##    def display(s,name,age):
##        s.email='r@gmail.com'
##        print(name,age,s.email)
##        print('python developer')
##
##    def show(s):
##        print(s.email)
##        s.display('raj',31)
##        print('java developer')
##
##    def demo(k):
##        print(k.email)
##        print(a.email)
##
##
##
##a=A()
##a.display('janvi',21)
##a.show()
##a.demo()
##


# destructor

# destructor is a member method of a class
# it delete the memory of object
#It can be call with object
# Name is _del_

# Garbage Collector:
# A program to delete reference
# It runs automatically
# it does memory management

##class A:
##    def _init_(self):
##        self.name='rajesh'
##        print('python developer')
##
##    def show(self):
##        print('java developer')
##
##    def _del_(self):
##        print('object deleted')
##
##   
##a=A()
##a.show()
##a.show()
##
##del a
##
##a.show()
##
##c=A()
##c.show()
##       
# Inheritance

# one class can inherit the properties and method of another class this process is known as inheritence

##class A:
##    a=10
##
##    def show(s):
##        print('python developer')
##
##
##class B(A):
##
##    b=20
##
##    def display(s):
##        print(s.b,s.a,B.b,B.a)
##        
##        print('java developer')
##
##
##
##
##c=B()
####print(c.b)
##c.display()

##print(c.a)
##c.show()


# types of inheritance:
#1) single level inheritance
#2) multilevel inh
#3) hirarchical inheritance
#4) Multiple inheritance
#5) Hybrid inheritance


#2)the inheritance in which a class can be derived from another derived class is known as multilevel inhet.(A==>B(A)===>c(B))

##class A:
##    a=10
##    def show(s):
##        print('Grand parent method called')
##
##class B(A):
##    b=20
##    def display(s):
##        print('parent method called')
##
##class C(B):
##    c=30
##    def data(s):
##        print(s.a+s.b+s.c)
##        print('chid method called')
##
##
##x=C()
##print(x.c)
##x.data()
##
##
##print(x.b)
##x.display()
##
##print(x.a)
##
##x.show()

#) Hirarchical inheritance===(one parent have multiple child)
# If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance.


##class A:
##    a=10
##    def show(s):
##        print('python developer')
##
##class B(A):
##    b=20
##    def display(s):
##        print('java developer')
##
##
##class C(A):
##    c=30
##    def demo(s):
##        print()
##        print('django developer')

##b=B()
##b.display()
##b.show()
##
##x=C()
##x.demo()
##x.show()

# Multiple inheritance
#  if a child class inherits from more than one class, i.e. this child
#  class is derived from multiple classes, we call it multiple
#  inheritance in Python.

##class A:
##    a=10
##    def show(s):
##        print('python developer')
##
##class B:
##    b=20
##    def display(s):
##        print('java developer')
##
##
##class C(A,B):
##    c=30
##    def demo(s):
##        print(s.c+s.b+s.a)
##        print()
##        print('django developer')
##
##x=C()
##x.demo()
##x.show()
##x.display()

##
##class Engineer:
##    def study(s):
##        print('Enginner study method called')
##
##    def show(s):
##        print('Enginner show method called')
##
##
##class Doctor:
##    def study(s):
##        print('doctor study method called')
##
##    def display(s):
##        print('doctor display method called')
##
##
##class student(Engineer,Doctor):
##    def demo(s):
##        print('Pharmacist')
##
##
##s=student()
##s.display()
##s.show()

#s.study()

    
class Engineer:
    def study(s):
        print('Enginner study method called')

    def show(s):
        print('Enginner show method called')


class Doctor:
    def study(s):
        print('doctor study method called')

    def display(s):
        print('doctor display method called')


class student(Doctor,Engineer):
    def demo(s):
        print('Pharmacist')


s=student()
##s.display()
##s.show()

s.study()



# Exceptional handeling An exception is an event, which occurs during
# the execution of a program, that interrupt the normal flow of the
# program's instructions.

##print('python developer')
##a=int(input('Enter the first number: '))
##b=int(input('Enter the second number: '))
##try:
##    print(a/b)
##except:
##    print('Exception handled')
##print('java developer')
##


##print('python developer')
##a=[11,22,3,64,35]
##
##try:
##    print(a[len(a)])
##except:
##    print('list index out of range')
##
##print('java developer')
##


##print('python developer')
##a=[11,22,3,64,35]
##
##try:
##    print(a[len(a)])
##except Exception as e:
##    print(e)
##
##print('java developer')
##


##print('python developer')
##try:
##    a=int(input('Enter the number: '))
##    b=int(input('Enter the number: '))
##    print(a/b)
##except Exception as e:
##    print(e)
##print('Hello')
##

##k=[]
##try:
##    print('thane')
##    #print(9/0)
##    #print(abc)
##    #print(k[2])
##    print(int('rajesh'))
##
##
##except ZeroDivisionError as e:
##    print('zero division',e)
##
##except NameError as e:
##    print(e)
##except IndexError as e:
##    print(e)
##except ValueError as e:
##    print(e)
##
##except Exception as e:
##    print(e)
##
##except:
##    print('Exception handeled')   # default except block must be last
##
##    


##try:
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    


##k=[]
##try:
##    print(k[2])
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    


##k=[11,22,33]
##try:
##    print(k[1])
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    
##else:
##    print('when exception is not occured')
##


##k=[]
##try:
##    print(k[1])
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(int('rajesh'))
##    except:
##        print('value Error')
##except:
##    print('Exception handeled outer try')
##    
##else:
##    print('when exception is not occured')
##finally:
##    print('it always be executed')
##

##try:
##    #print(9/0)
##    #print(abc)
##    print(int('rajesh'))
##
##except (ZeroDivisionError,NameError,ValueError) as e:
##    print(e)

##print('Hi')
##raise NameError()
##print('Hello')

##print('Hi')
##try:
##    
##    raise NameError()
##except:
##    print('Exception handle')
##print('Hello')

##
##class InvalidAgeError(Exception):
##    pass
##
##print('Hi')
##try:
##    raise InvalidAgeError()
##except:
##    print('Invalid age eror handled')
##print('Hello')
##


##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error handeled '
##
##print('Hi')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##print('Hello')

##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error handeled '
##
##print('Hi')
##try:
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##print('Hello')



##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error nfwefe'
##
##print('Hi')
##try:
##    
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##print('Hello')

##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error nfwefe'
##
##print('Hi')
##try:
##    
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##print('Hello')
##



##class InvalidAgeError(Exception):
##    msg='Invalid Age Error jkqbdwbd'
##    def _init_(self):
##        super()._init_(self.msg)
##
##print('Hi')
##try:
##    
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##print('Hello')



##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid Age Error detected'
##    
##
##age=int(input('Enter Your age: '))
##if age>=18:
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##    except Exception as e:
##        print(e)
##






##try:
##    print('thane')
##    try:
##        print(int('demo'))
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except:
##        print('exception handeled')
##except:
##    print('Outer exception handeled')
##
##

##k=[]
##try:
##    print(k[2])
##    try:
##        print(int('demo'))
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except:
##        print('exception handeled')
##except:
##    print('Outer exception handeled')
##




##k=[11,22,33,44]
##try:
##    print(k[1])
##    try:
##        print(int('demo'))
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except:
##        print('exception handeled')
##except:
##    print('Outer exception handeled')
##
##else:
##    print('it will execute when exception is not occured')



##k=[]
##try:
##    print(k[1])
##    try:
##        print(int('demo'))
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except:
##        print('exception handeled')
##except:
##    print('Outer exception handeled')
##
##else:
##    print('it will execute when exception is not occured')



##k=[11,22]
##try:
##    print(k[1])
##    try:
##        print(int('demo'))
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except:
##        print('exception handeled')
##except:
##    print('Outer exception handeled')
##
##else:
##    print('it will execute when exception is not occured')
##finally:
##    print('it always be executed')
##
##



##try:
##    #print(int('demo'))
##    #print(abc)
##    print(9/0)
##
##except (ValueError,NameError,ZeroDivisionError) as e:
##    print(e)


##print('thane')
##
##raise NameError
##
##    
##print('mumbai')



##print('thane')
##try:
##    raise NameError
##except:
##    print('exception handeled')
##print('mumbai')



##class InvalidAgeError(Exception):
##    pass
##
##
##print('thane')
##
##raise InvalidAgeError()
##
##print('mumbai')
##


##
##class InvalidAgeError(Exception):
##    pass
##
##
##print('thane')
##
##try:
##    raise InvalidAgeError()
##except:
##    print('Invalid Age Error')
##
##print('mumbai')
##
##




##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'invalid Age Error'
##
##
##print('thane')
##
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##
##print('mumbai')
##



##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'invalid Age Error'
##
##
##print('thane')
##
##try:
##    raise InvalidAgeError()
##except Exception as e:
##    print(e)
##
##print('mumbai')


##class InvalidAgeError(Exception):
##    def _str_(self):
##        return 'Invalid age detected Ypu can not vote'
##
##age=int(input('Enter your age: '))
##if(age>=18):
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##    except Exception as e:
##        print(e)
##
