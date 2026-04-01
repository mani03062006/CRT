'''a=[10,20,30,40,50]
print(a)
print(a[0])
print(a[-1])
b=list(10,20,312)
print(b)

a=[10,20,30,40,50]
print(a*2)
a=[10,20,30,40,50]
a.append(100)
print(a)
a.insert(1,50)
print(a)
#5)removing elements from list
a.remove(40)
print(a)
a.pop()
print(a)

#6)Slicing
a=[10,20,30,40,50]
print(a[0:])
print(a[2:])

#)reverse the list using slicing
print(a[::-1])

a=set([10,20,30,40,50])
print(a)

b=set([20,60,70,80])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
'''
t=(10,20,30,40,50)
print(t)
t1=tuple((10,20,30,40,50))
print(t1)
print(t[0])
print(t[-1])
print(t+t1)
print(tuple(t,t1))
print(t*3)
print(t[:0])
print(t1[1:3])
del t
print(t)