#scope : scope is a part of program in which variable can be used.
#local scope
#global scope

#Local variable: a variable can be declared inside the function call statement is called as local variable
#scope of local variable is inside the function only
'''
def display():
    a=10
    print(a)

display()
'''

# global variable: a variable can be declared outside the function is called as global variable
#scope of global variable is inside as well as outside the function
'''
A=66
def display():
    a=7
    b=9
    print(a)
    print(A)

print(A)
display()
print(A)
'''
'''
A=30
def display():
    A=30
    print(A)
print(A)
display()
print(A)
'''
'''
A=30
def display():
    global A
    A=50
    print(A)
print(A)
display()
print(A)
'''
'''
B=30
def display(x):
    global a
    a=a+x
    return a

a=20
b=5
display(b)
print(a)
'''


##a=10
##y=5
##def myfun():
##    a=2
##    y=a
##    print(y,a)
##
##myfun()
##print(y,a)



##a=10
##y=5
##def myfun():
##    global a
##    y=a
##    a=2
##    print(y,a)
##
##myfun()
##print(y,a)

'''
a=10
y=5
def myfun():
    global a
    y=a
    a=2
    print(y,a)

myfun()
print(y,a)
'''

'''
a=10
y=5
def myfun():
    global a
    a=2
    y=a
    print(y,a)

myfun()
print(y,a)
'''

##a=1
##def display():
##    return a
##print(a)
##print(display())
##print(a)



    
