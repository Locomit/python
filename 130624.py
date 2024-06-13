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


    
