#l=[1,2,3,4]
#x=len(l)
#for i in range(x):
 #   print(i,l[i])


#dd={'a':100, 'b':200,' c':300}
#print(dd)

d={}
n=int(input("Enter no. of  elements:"))
for i in range(n):
    k=input("Enter key:")
    v=input("Enter values:")
    d.update({k:v})
print("new dictionary:",d)