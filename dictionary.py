#dictionary methods
a = {'name':'namita','age':32,'city':'titwala'}
print(a['name'])
print(a.get('name'))
print(a.get('age'))


a['phone']=987654321
a.update({'tel':78945623})

a.pop('name')
a.popitem()
del a['age']

print(a)
