set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
#union
c=set1 | set2
#c=set1.union(set2)
print(c)

#Intersection
a=set1 & set2
#a=set1.intersection(set2)
print(a)

#intersection update
set2.intersection_update(set1)
print(set1)
print(set2)

#difference
b=set1.difference(set2)
print(b)

#difference update
set1.difference_update(set2)
print(set1)
print(set2)

#symmetric difference in this all values are combine without repeting
c=set1 ^ set2
#c=set1.symmetric_difference(set2)
print(c)

#symmetric difference
set1.symmetric_difference_update(set2)
print(set1)
print(set2)

#subset
set4={1,2,3}
set5={1,2,3,5,6,7,8}
#is_subset=set4.issubset(set5)
is_subset=set5.issuperset(set4)
print(is_subset)

