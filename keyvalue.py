d={}
n=int(input("Enter no. of  elements:"))
for i in range(n):
    k=input("Enter key:")
    v=input("Enter values:")
    d.update({k:v})
print("new dictionary:",d)