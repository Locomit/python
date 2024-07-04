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

class A:
    a=10
    b=20

    def demo(s):
        s.a= s.a+1
        A.b= A.b+1

        print(s.a, A.b)
x=A()
x.demo()

y=A()
y.demo()

z=A()
z.demo()



