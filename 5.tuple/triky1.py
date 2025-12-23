a = (1,2,3)
a = list(a)
a.append(4)
a = tuple(a)
print(a)
print(type(a))

z,x,y = a[0], a[1], a[2]
print(z,x,y)