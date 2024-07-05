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

# __str__ : str method is used when method will get printed


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




























