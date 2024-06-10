a={'a':100, 'b':200, 'c':300}

a.clear()
print(a)

b={'a':100, 'b':200, 'c':300}
print(b)

c={'a':1, 'b':[2,3], 'c':55}
cc=c.copy()
c['b'][0]=45
cc[2]=69
print(cc)
print(c)

#get access values
value=c.get('b')
print(value)

#access only item
value1=c.items()
print(value1)

#access only keys
values2=c.keys()
print(values2)

#access only values
value3=c.values()
print(value3)

#pop
value4=c.pop('c')
print(value4)

#popitem
value5=c.popitem()
print(value5)

#update
dict1={'a':1, 'b':2}
dict2={'b':7, 'c':4}
dict1.update(dict2)
dict1.update({'d':106})
print(dict1)