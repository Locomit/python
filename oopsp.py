#Local variable will define only in their method class it will not perform in another method.
##class A:
##    def show(self,roll_no,dept):
##        print(roll_no,dept)
##        name='Namita'
##        age=23
##        print(name, age)
##    def display(self):
##        email='n@gmail.com'
##        branch='Comp'
##        print(email,branch)
##a=A()
##a.show(12,'mech')
###print(a.name)
##a.display()

# Instance variable are accessible in both methods or different methods.


##class A:
##    def show(self,name,age,salary):
##        a.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(a.name1,self.age1,self.salary1)
##
##    def display(self):
##        print(a.name1,self.age1,self.salary1)
##a=A()
##a.show('Robin',24,1700000)
##a.display()


##class A:
##  name='namita'
##    def show(self,name,age,salary):
##        a.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(a.name1,self.age1,self.salary1)
##
##    def display(self):
##        print(a.name1,self.age1,self.salary1)
##a=A()
##a.show('Robin',24,1700000)
##a.display()

#Static variable

##class A:
##    name='Sanji'
##
##    def show(s):
##        print(A.name)
##        
##
##s=A()
##s.show()

##class A:
##    def show(self,name,address):
##        print('Python Developer')
##    def display(self):
##        self.show('robin','skypedia')
##        a.show('Sanji','Thane')
##        print('Java developer')
##a=A()
##a.show('Nams','Ambivali')
##a.display()

##class A:
##    def show(self):
##        self.name=input('Enter your name: ')
##        self.age=int(input('Enter your age: '))
##
##    def display(self):
##        print('your name is ',self.name)
##        print('your age is ',self.age)
##
##a=A()
##a.show()
##a.display()

#static variable can change but instance variable can be updated

##class A:
##    a=10
##    b=20
##
##    def demo(s):
##        s.a= s.a+1
##        A.b= A.b+1
##
##        print(s.a, A.b)
##x=A()
##x.demo()
##
##y=A()
##y.demo()
##
##z=A()
##z.demo()
##


# Constructor: __init__ method runs automatically when object is created which is used to initialize the instance object

##class A:
##    def __init__(s):
##        print('Namita')
##        s.id=10
##        s.name='Robin'
##        s.salary=50000
##
##    def display(s):
##        print('id is: ',s.id)
##        print('name is: ',s.name)
##        print('Salary is: ',s.salary)
##
##a=A()
##a.display()


##class A:
##    def __init__(s):
##        s.id=int(input('Enter Id: '))
##        s.name=input('Enter the name: ')
##
##    def display(s):
##        print('Your id is ',s.id)
##        print('Your name is ',s.name)
##
##
##a=A()
##a.display()

##class A:
##    def __init__(s):
##        s.id=int(input('Enter id: '))
##        s.name=input('Enter your name: ')
##        s.salary=int(input('Enter yout salary:'))
##
##    def display(s):
##        print(f'id is {s.id} name is {s.name} and salary is {s.salary}.')
##
##a=A()
##a.display()


##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name, s.age, s.salary)
##
##a=A('Sanji',28,680000)
##a.display()


# __str__ : str method is used when method will get printed.

##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##
##    def display(s):
##        print(s.name, s.age, s.salary)
##
##    def __str__(s):
##        return s.name+' '+str(s.age)+' '+str(s.salary)
##
##a=A('Robin', 24,800000)
##a.display()
##
##print(a)




##class A:
##    def display(s,name,age):
##        s.email='n@gmail.com'
##        print(name,age,s.email)
##        print('python Developer')
##
##    def show(s):
##        print(s.email)
##        s.display('Robin',24)
##        print('java developer')
##
##    def demo(k):
##        print(k.email)
##        print(a.email)
##
##a=A()
##a.display('Zoro',27)
##a.show()
##a.demo()


#destructor: it is a member method of a class it delete the memory of object it can be call with object name is __ del__
#it also called as a garbage collector a program to delete reference it runs automatically.

##class A:
##    def __init__(self):
##        self.name='Zoro'
##        print('Python developer')
##
##    def show(self):
##        print('Java developer')
##
##    def __del__(self):
##        print('Object is deleted')
##
##a=A()
##a.show()
##
####del a
####a.show()
##
##c=A()
##c.show()


#Inheritance : one class can inherit the properties and method of another class this process is known as inheritence

##class A:
##    a=10
##
##    def show(s):
##        print('Python Developer')
##
##class B(A):
##    b=20
##    def display(s):
##        print(s.b, c.b, c.a, B.a, B.b)
##        print('Java developer')
##
##c=B()
##c.display()


# Types of inheritance
##single level
##multilevel
##hirarchical
##multiple
##Hybrid

#2)the inheritance in which a class can be derived from another derived class is known as multilevel inheritance

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
##        print('child method called')
##
##x=C()
##x.data()

#3)


##Polymorphism
##polymorphism means many form
##an entity can workk in multiple role this capability is called as polymorphism
##1. function overriding
##2. function overloading
##
##1. In function overriding we can declare a function in base calss and derived calss with same name and same parameter
##it occures when one class is inherit from another class

##class A:
##    def display(self):
##        print('python developer')
##
##class B(A):
##    def display(self):
##        print('Java developer')
##
##ob=B()
##ob.display()

##function overloading
##more than one function with same name defined in same class and call with different parameter
##this process is known as method overloading.
##but python does not support method overloading. it support in java

##class A:
##    def show(self):
##        print('hii')
##    def show(self,x,y):
##        print('bye')
##    def show(self):
##        print('helllooooo')
##
##a=A()
##
##a.show()
##a.show(10)
##a.show(10,20)


##class A:
##    def show(self,x,y):
##        print(x+y)
##a=A()
##a.show(10,30)

##class A:
##    def show(self, a=None, b=None, c=None):
##        if(a!=None and b!=None and c!=None):
##            print(a+b+c)
##        elif(a!=None and b!=None):
##            print(a+b)
##        else:
##            print(a)
##
##d=A()
##d.show(10)
##d.show(2,3)
##d.show(10,20,30)

#Possibility for overloading in python

#Handling

##print('Thane')
##try:
##    raise InvalidAgeError()
##except:
##    print('exception handelled')
##print('Mumbai')
##

##class InvalidAgeError(Exception):
##    pass
##print('thane')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print('exception Handled')
##print('Mumbai')

##class InvalidAgeError(Exception):
##    def __str__(self):
##        return 'Invalid Age Error Detected'
##print('Thane')
##try:
##    raise InvalidAgeError()
##except InvalidAgeError as e:
##    print(e)
##print('mumbai')

##class InvalidAgeError(Exception):
##    def __str__(self):
##        return 'Invalid age detected'
##
##age=int(input('Enter your age:'))
##if(age>=18):
##    print('You can vote')
##else:
##    try:
##        raise InvalidAgeError()
##
##    except InvalidAgeError as e:
##        print(e)
##

##class A:
##    def __init__(self,name,age):
##        print('python developer')
##        print(name,age)
##    def show(self):
##        print('Hii')
##
##class B(A):
##    def __init__(self,name,age):
##        super().__init__('raj',32)
##        print('java developer')
##        print(name,age)
##    def display(self):
##        print('Hello')
##
##b=B('Rajesh',31)
##    

























